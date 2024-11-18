from django.urls import path
from HAStudio import views

urlpatterns = [
    path('', views.index, name='index'),
    path('services', views.services, name='services'),
    path('registration', views.registration, name='registration'),
    path('contacts', views.contacts, name='contacts'),
    path('about', views.about, name='about'),
    path('posts', views.PostListView.as_view(), name='post_list'),
    path('<slug:slug>', views.PostDetailView.as_view(), name='post_detail'),
]
