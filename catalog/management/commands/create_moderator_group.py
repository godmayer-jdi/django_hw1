from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist
from catalog.models import Product


class Command(BaseCommand):
    help = 'Создает группу "Модератор продуктов" с правами'

    def handle(self, *args, **options):
        # Создать группу
        group, created = Group.objects.get_or_create(name='Модератор продуктов')
        group.permissions.clear()  # Очистка существующие прав

        content_type = ContentType.objects.get_for_model(Product)

        # Добавление прав
        content_type = ContentType.objects.get_for_model(Product)
        permissions_to_add = []

        # Право can_unpublish_product
        unpublish_perm, _ = Permission.objects.get_or_create(
            codename='can_unpublish_product',
            name='Может отменять публикацию продукта',
            content_type=content_type
        )
        permissions_to_add.append(unpublish_perm)

        # Право delete_product
        try:
            delete_perm = Permission.objects.get(
                codename='delete_product',
                content_type=content_type
            )
            permissions_to_add.append(delete_perm)
        except ObjectDoesNotExist:
            self.stdout.write(self.style.WARNING('Право delete_product не найдено'))

        # Добавить права группе
        group.permissions.set(permissions_to_add)

        action = 'создана' if created else 'обновлена'
        self.stdout.write(
            self.style.SUCCESS(f'Группа "Модератор продуктов" {action}')
        )
        self.stdout.write(
            self.style.SUCCESS(
                f'Права ({len(permissions_to_add)}): {", ".join([p.codename for p in permissions_to_add])}')
        )
