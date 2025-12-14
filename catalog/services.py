from .models import Product, Category
from django.core.cache import cache


def get_products_by_category(category_id):
    """Сервис: продукты по категории - кэшширование"""
    cache_key = f'category_products_{category_id}'
    products = cache.get(cache_key)

    if products is None:
        products = Product.objects.filter(
            category_id=category_id,
            is_published=True
        ).select_related('category', 'owner').order_by('-created_at')
        cache.set(cache_key, products, 60 * 15)  # 15 минут

    return products