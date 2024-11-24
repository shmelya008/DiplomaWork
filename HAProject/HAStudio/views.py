from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, SignUpForm
from .models import Post, UserProfile, Report
from django.contrib.auth.models import User
from .telegram_utils import send_telegram_message


# Create your views here.
def index(request):
    text_head = 'Это заголовок главной страницы сайта'
    text_body = 'Добро пожаловать на сайт студии HairAprel! Это содержимое главной страницы сайта'
    context = {'text_head': text_head, 'text_body': text_body}
    return render(request, 'index.html', context)


def about(request):
    text_head = 'Сведения о компании'
    context = {'text_head': text_head}
    return render(request, 'about.html', context)


def contacts(request):
    text_head = 'Контакты'
    name = 'Студия наращивания волос "HairAprel"'
    address = 'Санкт-Петербург, ул.Социалистическая, д.21'
    tel = '+7(812) 227-23-24'
    email = 'example@mail.ru'
    context = {'text_head': text_head, 'name': name, 'address': address, 'tel': tel, 'email': email}
    return render(request, 'contacts.html', context)


def services(request):
    user = User()
    name = 'Мы предоставляем следующие услуги:"'
    service1 = 'наращивание волос. описание услуги'
    service2 = 'Окрашивание волос'
    service3 = 'Стрижка укладка волос'
    service4 = 'Трихология'
    context = {'user': user, 'name': name, 'service1': service1,
               'service2': service2, 'service3': service3, 'service4': service4}
    return render(request, 'services.html', context)


def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # сохранение номера
            UserProfile.objects.create(user=user, phone_number=form.cleaned_data.get('phone_number'),
                                       requested_service=form.cleaned_data.get('requested_service'))
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('service_response')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def service_response(request):
    return render(request, 'service_response.html')


def reg_auth(request):
    return render(request, 'reg_auth.html')


@login_required
def user_logout(request):
    logout(request)
    return render(request, 'logged_out.html', {})


class PostListView(ListView):
    queryset = Post.objects.filter(status='published')
    context_object_name = 'posts'
    paginate_by = 2
    template_name = 'post_list.html'


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'post_detail.html'


def send_post_to_telegram_view(request):
    report = Report.objects.first()
    send_telegram_message(chat_id='settings/CHAT_ID', report=report)
    return redirect('service_response')


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

