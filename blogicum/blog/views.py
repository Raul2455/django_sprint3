"""Модуль представлений для блога."""

from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from django.utils import timezone

from blog.models import Post, Category


def index(request):
    """Отображение главной страницы."""
    post_list = Post.objects.select_related(
        'location', 'author', 'category'
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__date__lt=timezone.now()
    )[:5]
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def post_detail(request, id_post):
    """Отображение отдельного поста."""
    posts = get_object_or_404(Post.objects.select_related(
        'location', 'author', 'category'
    ).filter(Q(pub_date__date__lt=timezone.now())
             & Q(is_published=True)
             & Q(category__is_published=True)
             ), pk=id_post)
    context = {'post': posts}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    """Отображение постов по отдельной категории."""
    post_list = Post.objects.select_related(
        'location', 'author', 'category',
    ).filter(
        category__slug=category_slug,
        is_published=True,
        pub_date__date__lt=timezone.now(),
    )
    category = Category.objects.values(
        'title', 'description', 'slug'
    ).filter(slug=category_slug)
    category = get_object_or_404(
        Category.objects.values(
            'title', 'description', 'slug', 'is_published',
        ).filter(is_published=True), slug=category_slug)
    context = {'post_list': post_list, 'category': category}
    return render(request, 'blog/category.html', context)
