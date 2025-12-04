from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import ProductForm, ContactForm
from .models import Product


class HomeView(TemplateView):
    template_name = "catalog/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all()
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


class ProductDetailView(TemplateView):
    template_name = "catalog/product_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = kwargs.get("pk")
        context["product"] = get_object_or_404(Product, pk=pk)
        return context


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, 'Продукт успешно создан!')
        return super().form_valid(form)

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, 'Продукт успешно обновлен!')
        return super().form_valid(form)

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('home')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Продукт успешно удален!')
        return super().delete(request, *args, **kwargs)
