"""Модуль, содержащий менеджеры моделей для приложения блог."""

from django.db.models import Manager
from django.utils.timezone import now


class PostManager(Manager):
    """Менеджер модели Post, возвращающий только опубликованные посты."""

    def published(self):
        """Метод для получения только опубликованных постов
        через select_related."""
        return self.get_queryset().filter(
            is_published=True,
            pub_date__lt=now(),
            category__is_published=True
        ).select_related('author', 'category', 'location')
