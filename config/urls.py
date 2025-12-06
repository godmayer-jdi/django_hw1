from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "", include("catalog.urls")
    ),  # подключаем маршруты приложения catalog по корню сайта
    path(
        "blogs/", include("blog.urls")
    ),  # подключаем маршруты приложения blog по корню сайта
    path(
        "users/", include("users.urls")
    ),  # подключаем маршруты приложения users по корню сайта
]
