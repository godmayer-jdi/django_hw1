from django import forms


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
