from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from blog.models import BlogPost  # Предполагаемая модель


class Command(BaseCommand):
    help = 'Создает группу "Контент-менеджер" для блога'

    def handle(self, *args, **options):
        group, created = Group.objects.get_or_create(name='Контент-менеджер')

        content_type = ContentType.objects.get_for_model(BlogPost)
        permissions = Permission.objects.filter(content_type=content_type)
        group.permissions.set(permissions)

        self.stdout.write(
            self.style.SUCCESS(f'Группа "Контент-менеджер" {"создана" if created else "обновлена"}')
        )
