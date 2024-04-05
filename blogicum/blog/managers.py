"""Модуль, содержащий менеджеры моделей для приложения блог."""

from django.db.models import Manager, QuerySet
from django.utils.timezone import now


class PostManager(Manager):
    """
    Менеджер модели Post, возвращающий только опубликованные посты.
    """

    def get_queryset(self) -> QuerySet:
        """
        Переопределение метода get_queryset для возврата
        только опубликованных постов.
        """
        return (
            super()
            .get_queryset()
            .filter(is_published=True, pub_date__lt=now(),
                    category__is_published=True)
            .select_related('author', 'category', 'location')
        )

    def published(self) -> QuerySet:
        """
        Метод для получения только опубликованных постов.
        """
        return self.get_queryset()
