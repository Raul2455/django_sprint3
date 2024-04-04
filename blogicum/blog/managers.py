"""Модуль, содержащий менеджеры моделей для приложения блог."""

from django.db.models import Manager, QuerySet
from django.utils.timezone import now


class PostManager(Manager):
    """Менеджер модели Post, который возвращает только опубликованные посты."""

    def get_queryset(self) -> QuerySet:
        """Возвращает QuerySet,только опубликованные посты."""
        return super().get_queryset().filter(
            is_published=True, pub_date__lt=now(),
            category__is_published=True
        ).select_related('author', 'category', 'location')
