from django.contrib import messages
from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from .forms import (CustomAuthenticationForm, CustomUserCreationForm,
                    UserProfileForm)


class UserRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "users/register.html"
    success_message = "Регистрация прошла успешно! Добро пожаловать!"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        # Отправка приветственного письма (console backend)
        user.email_user(
            subject="Добро пожаловать в Skystore!",
            message=f"Привет, {user.username}!\n\nВы успешно зарегистрировались в Skystore.\nВаш email: {user.email}",
        )

        return redirect("catalog:product_list")


class UserLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = "users/login.html"


class UserLogoutView(LogoutView):
    next_page = "/"


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = UserProfileForm
    template_name = "users/profile_edit.html"

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        messages.success(self.request, "Профиль обновлен!")
        return reverse_lazy("catalog:product_list")
