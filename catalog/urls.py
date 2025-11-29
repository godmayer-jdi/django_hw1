from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # корень сайта будет вести на views.home
    path("contacts/", views.contacts, name="contacts"),
    path("product_detail/<int:pk>/", views.product_detail, name="product_detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
