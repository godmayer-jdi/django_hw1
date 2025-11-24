from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "", include("catalog.urls")
    ),  # подключаем маршруты приложения catalog по корню сайта
]
