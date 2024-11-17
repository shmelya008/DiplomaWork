from django.shortcuts import render, get_object_or_404
from .models import Post


# Create your views here.
def index(request):
    text_head = 'Это заголовок главной страницы сайта'
    text_body = 'Это содержимое главной страницы сайта'
    context = {'text_head': text_head, 'text_body': text_body}
    return render(request, 'index.html', context)


def services(request):
    return render(request, 'services.html')


def post_list(request):
    posts = Post.objects.filter(status='published')
    return render(request, 'post_list.html', {'posts': posts})


def post_detail(request, post):
    post = get_object_or_404(Post, slug=post, status='published')
    return render(request, 'post_detail.html', {'post': post})

