from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, ListView,
                                  TemplateView, UpdateView)

from .forms import ContactForm, ProductForm
from .models import Product, Category
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.cache import cache
from .services import get_products_by_category


class HomeView(TemplateView):
    template_name = "catalog/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.filter(
            is_published=True
        )  # Только опубликованные
        return context


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == "POST":
            context["form"] = ContactForm(self.request.POST)
            if context["form"].is_valid():
                context["form"].save()
                context["success_message"] = "Спасибо за сообщение!"
                context["form"] = ContactForm()  # Очистка формы
        else:
            context["form"] = ContactForm()
        return context

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)  # Обрабатываем POST как GET


@method_decorator(cache_page(60 * 5), name='dispatch')  #Добавлен декоратор. Кэш 5 мин
class ProductDetailView(TemplateView):
    template_name = "catalog/product_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = kwargs.get("pk")
        context["product"] = get_object_or_404(Product, pk=pk)
        return context


class ProductListView(ListView):
    model = Product
    template_name = "catalog/product_list.html"
    context_object_name = "products"

    def get_queryset(self):
        return Product.objects.filter(is_published=True)  # Только опубликованные


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        messages.success(self.request, "Продукт успешно создан!")
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name="Модератор продуктов").exists():
            return Product.objects.all()
        return Product.objects.filter(owner=user)

    def form_valid(self, form):
        messages.success(self.request, "Продукт успешно обновлен!")
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:product_list")

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name="Модератор продуктов").exists():
            return Product.objects.all()
        return Product.objects.filter(owner=user)

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Продукт успешно удален!")
        return super().delete(request, *args, **kwargs)


class ProductCategoryView(ListView):
    template_name = "catalog/product_category.html"
    context_object_name = "products"

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return get_products_by_category(category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs['category_id']
        context['category'] = get_object_or_404(Category, id=category_id)
        return context
