from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post, Category


def index(request):
    post_list = Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__isnull=False
    ).order_by('-pub_date')
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/index.html', {'page_obj': page_obj})


def post_detail(request, post_id):
    post = get_object_or_404(
        Post.objects.filter(
            is_published=True,
            category__is_published=True,
            pub_date__isnull=False
        ),
        id=post_id
    )
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__isnull=False
    ).order_by('-pub_date')
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/category.html', {'category_slug': category_slug, 'page_obj': page_obj})
