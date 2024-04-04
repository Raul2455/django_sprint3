from django.db import models


class PublishedModel(models.Model):
    """Абстрактная модель. Добвляет флаг is_published и дату время."""

    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
        blank=True,
        help_text='Снимите галочку, чтобы скрыть публикацию.',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        verbose_name='Добавлено',
    )

    class Meta:
        abstract = True
