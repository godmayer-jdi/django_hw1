from django.db import models


class Category(models.Model):
    """Создаем модель Category"""

    objects = models.Manager()
    name = models.CharField("Наименование", max_length=255)
    description = models.TextField("Описание")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    """Создаем модель Product"""

    objects = models.Manager()
    name = models.CharField("Наименование", max_length=255)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="products/")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Категория"
    )
    price = models.DecimalField("Цена за покупку", max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name
