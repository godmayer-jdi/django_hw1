from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.views.generic import CreateView

from .forms import CustomUserCreationForm, CustomAuthenticationForm


class UserRegisterView(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = '/'
    success_message = 'Регистрация прошла успешно! Добро пожаловать!'

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        # Отправка приветственного письма (console backend)
        user.email_user(
            subject='Добро пожаловать в Skystore!',
            message=f'Привет, {user.username}!\n\nВы успешно зарегистрировались в Skystore.\nВаш email: {user.email}'
        )
        login(self.request, user)
        return response


class UserLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'users/login.html'
