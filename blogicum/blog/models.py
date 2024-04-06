from django.db import models
from django.contrib.auth import get_user_model

# Импортируем кастомный менеджер для модели Post
from .managers import PostManager

User = get_user_model()

MAX_LENGTH_TITLE = 256  # Константа для максимальной длины заголовка


class PublishedModel(models.Model):
    """Абстрактная модель. Добавляет флаг is_published и дату-время."""

    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено',
    )

    class Meta:
        abstract = True


class Category(PublishedModel):
    """Категория публикаций в блоге."""

    title = models.CharField(
        max_length=MAX_LENGTH_TITLE,
        blank=True,
        verbose_name='Заголовок',
    )
    description = models.TextField(
        blank=True,
        verbose_name='Описание',
    )
    slug = models.SlugField(
        blank=True,
        unique=True,
        verbose_name='Идентификатор',
        help_text=('Идентификатор страницы для URL; разрешены символы '
                   'латиницы, цифры, дефис и подчёркивание.')
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'
        default_related_name = 'categories'

    def __str__(self):
        return self.title[:50]


class Location(PublishedModel):
    """Местоположение, связанное с публикацией в блоге."""

    name = models.CharField(
        max_length=MAX_LENGTH_TITLE,
        blank=True,
        verbose_name='Название места',
    )

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'
        default_related_name = 'locations'

    def __str__(self):
        return self.name[:50]


class Post(PublishedModel):
    """Публикация в блоге."""

    title = models.CharField(
        max_length=MAX_LENGTH_TITLE,
        verbose_name='Заголовок',
    )
    text = models.TextField(
        verbose_name='Текст',
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата и время публикации',
        help_text='Если установить дату и время в будущем — можно делать '
                  'отложенные публикации.'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор публикации',
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,  # Разрешаем создание поста без привязки к локации
        verbose_name='Местоположение',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Категория',
    )

    # Вот здесь мы добавляем кастомный менеджер модели
    objects = PostManager()

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        ordering = ['-pub_date']  # Сортировка от новых к старым
        default_related_name = 'posts'

    def __str__(self):
        return self.title[:50]
