from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # корень сайта будет вести на views.home
    path('home/', views.home, name='home'),  # дополнительный путь home/
    path('contacts/', views.contacts, name='contacts'),
]
