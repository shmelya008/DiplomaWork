from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .models import Post


# Create your views here.
def index(request):
    text_head = 'Это заголовок главной страницы сайта'
    text_body = 'Добро пожаловать на сайт студии air April! Это содержимое главной страницы сайта'
    context = {'text_head': text_head, 'text_body': text_body}
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def contacts(request):
    return render(request, 'contacts.html')


def services(request):
    return render(request, 'services.html')


class PostListView(ListView):
    queryset = Post.objects.filter(status='published')
    context_object_name = 'posts'
    paginate_by = 2
    template_name = 'post_list.html'

    # def post_list(request):
    #     posts = Post.objects.filter(status='published')
    #     paginator = Paginator(posts, 3)
    #     page = request.GET.get('page')
    #     try:
    #         posts = paginator.page(page)
    #     except PageNotAnInteger:
    #         posts = paginator.page(1)
    #     except EmptyPage:
    #         posts = paginator.page(paginator.num_pages)
    #     return render(request, 'post_list.html', {'page': page, 'posts': posts})


def registration(request):
    return render(request, 'registration.html')


def post_detail(request, post):
    post = get_object_or_404(Post, slug=post, status='published')
    return render(request, 'post_detail.html', {'post': post})

