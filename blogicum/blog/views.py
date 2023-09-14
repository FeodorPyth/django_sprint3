import datetime

from django.shortcuts import get_object_or_404, render

from .models import Post, Category


def common_request():
    return Post.objects.filter(
        pub_date__lte=datetime.datetime.now(),
        is_published=True,
        category__is_published=True
    )


def index(request):
    template_name = 'blog/index.html'
    post_list = common_request()[:5]
    context = {'post_list': post_list, }
    return render(request, template_name, context)


def post_detail(request, id):
    template_name = 'blog/detail.html'
    post = get_object_or_404(
        common_request(),
        pk=id
    )
    context = {'post': post, }
    return render(request, template_name, context)


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    category = get_object_or_404(
        Category.objects.filter(
            is_published=True,
        ),
        slug=category_slug
    )
    post_list = category.posts.filter(
        is_published=True,
        pub_date__lte=datetime.datetime.now()
    )
    context = {
        'category': category,
        'post_list': post_list,
    }
    return render(request, template_name, context)
