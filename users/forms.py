from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'email@example.com *'
        })
    )

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = user.email
        if commit:
            user.save()
        return user

'''    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class': 'form-control form-control-lg',
            'placeholder': 'email@example.com *'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control form-control-lg',
            'placeholder': 'Пароль *'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control form-control-lg',
            'placeholder': 'Повторите пароль *'
        })
'''

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control form-control-lg',
            'placeholder': 'Ваш email'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control form-control-lg',
            'placeholder': 'Пароль'
        })

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['avatar', 'phone', 'country']
        widgets = {
            'phone': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': '+7 (___) ___-__-__'
            }),
            'country': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Россия'
            }),
        }
        labels = {
            'avatar': 'Аватар',
            'phone': 'Телефон',
            'country': 'Страна'
        }

    def clean_avatar(self):
        avatar = self.cleaned_data.get('avatar')
        if avatar:
            if avatar.size > 2 * 1024 * 1024:  # 2MB
                raise ValidationError('Размер аватара не более 2MB!')
            if not avatar.name.lower().endswith(('.jpg', '.jpeg', '.png')):
                raise ValidationError('Только JPG/PNG!')
        return avatar
