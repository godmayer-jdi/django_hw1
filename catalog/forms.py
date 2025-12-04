from django import forms
from django.core.exceptions import ValidationError
from .models import Product


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="Имя",
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Ваше имя *",
                "required": True,
            }
        ),
    )

    phone = forms.CharField(
        max_length=20,
        required=False,
        label="Телефон",
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "+7 (___) ___-__-__",
            }
        ),
    )

    message = forms.CharField(
        label="Сообщение",
        widget=forms.Textarea(
            attrs={
                "class": "form-control form-control-lg",
                "rows": 5,
                "placeholder": "Расскажите подробнее... *",
                "required": True,
            }
        ),
    )

    def save(self):
        """Сохранить данные формы (логирование/БД/почта)"""
        print(
            f"Новое сообщение от {self.cleaned_data['name']}: {self.cleaned_data['message']}"
        )
        return self.cleaned_data

# Константы запрещенных слов
FORBIDDEN_WORDS_NAME = ['казино', 'криптовалюта', 'крипта', 'биржа',
                       'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
FORBIDDEN_WORDS_DESCRIPTION = ['казино', 'криптовалюта', 'крипта', 'биржа',
                              'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Название продукта *'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control form-control-lg',
                'rows': 4,
                'placeholder': 'Описание продукта *'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control form-control-lg'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select form-select-lg'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': '0.00',
                'step': '0.01'
            }),
        }
        labels = {
            'name': 'Название',
            'description': 'Описание',
            'image': 'Изображение',
            'category': 'Категория',
            'price': 'Цена (руб.)'
        }

    def __init__(self, *args, **kwargs):
        """Стилизация форм в стиле Bootstrap"""
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = True  # Все поля обязательны

    def clean_name(self):
        """Валидация названия на запрещенные слова"""
        name = self.cleaned_data['name'].lower()
        forbidden = [word for word in FORBIDDEN_WORDS_NAME if word in name]
        if forbidden:
            raise ValidationError(f'Запрещенные слова в названии: {", ".join(forbidden)}')
        return self.cleaned_data['name']
