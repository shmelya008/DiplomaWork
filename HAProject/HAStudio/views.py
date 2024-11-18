from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView
from .models import Post


# Create your views here.
def index(request):
    text_head = 'Это заголовок главной страницы сайта'
    text_body = 'Добро пожаловать на сайт студии HairAprel! Это содержимое главной страницы сайта'
    context = {'text_head': text_head, 'text_body': text_body}
    return render(request, 'index.html', context)


def about(request):
    text_head = 'Сведения о компании'
    name = 'Студия наращивания волос "HairAprel"'
    service1 = 'Наращивание волос'
    service2 = 'Окрашивание волос'
    service3 = 'Стрижка укладка волос'
    service4 = 'Трихология'
    context = {'text_head': text_head, 'name': name, 'service1': service1,
               'service2': service2, 'service3': service3, 'service4': service4}
    return render(request, 'about.html', context)


def contacts(request):
    text_head = 'Контакты'
    name = 'Студия наращивания волос "HairAprel"'
    address = 'Санкт-Петербург, ул.Социалистическая, д.21'
    tel = '+7(812) 227-**-**'
    email = 'example@mail.ru'
    context = {'text_head': text_head, 'name': name, 'address': address, 'tel': tel, 'email': email}
    return render(request, 'contacts.html', context)


def services(request):
    return render(request, 'services.html')


def registration(request):
    return render(request, 'registration.html')


class PostListView(ListView):
    queryset = Post.objects.filter(status='published')
    context_object_name = 'posts'
    paginate_by = 2
    template_name = 'post_list.html'


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'post_detail.html'


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

# def post_detail(request, post):
#     post = get_object_or_404(Post, slug=post, status='published')
#     return render(request, 'post_detail.html', {'post': post})

