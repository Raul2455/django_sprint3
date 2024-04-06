"""Модуль, содержащий менеджеры моделей для приложения блог."""

from django.db.models import Manager
from django.utils.timezone import now


class PostManager(Manager):
    """Менеджер модели Post для возвращения опубликованных постов."""

    def published(self):
        """
        Возвращает опубликованные посты с использованием select_related.
        """
        return self.get_queryset().filter(
            is_published=True,
            pub_date__lt=now(),
            category__is_published=True
        ).select_related('author', 'category', 'location')
