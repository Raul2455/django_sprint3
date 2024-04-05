from django.shortcuts import get_object_or_404, render
from blog.models import Post, Category

POSTS_PER_PAGE = 5


def index(request):
    """Отображение главной страницы."""
    post_list = Post.objects.published()[:POSTS_PER_PAGE]
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def post_detail(request, id_post):
    """Отображение отдельного поста."""
    post = get_object_or_404(Post.objects.published(), pk=id_post)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    """Отображение постов по отдельной категории."""
    category = get_object_or_404(
        Category.objects.filter(is_published=True), slug=category_slug
    )
    post_list = Post.objects.published().filter(
        category=category
    )[:POSTS_PER_PAGE]
    context = {'post_list': post_list, 'category': category}
    return render(request, 'blog/category.html', context)
