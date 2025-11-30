from django.views.generic import TemplateView

from django.shortcuts import get_object_or_404

from .models import Product

from .forms import ContactForm


class HomeView(TemplateView):
    template_name = 'catalog/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == 'POST':
            context['form'] = ContactForm(self.request.POST)
            if context['form'].is_valid():
                context['form'].save()
                context['success_message'] = 'Спасибо за сообщение!'
                context['form'] = ContactForm()  # Очистка формы
        else:
            context['form'] = ContactForm()
        return context

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)  # Обрабатываем POST как GET


class ProductDetailView(TemplateView):
    template_name = 'catalog/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = kwargs.get('pk')
        context['product'] = get_object_or_404(Product, pk=pk)
        return context
