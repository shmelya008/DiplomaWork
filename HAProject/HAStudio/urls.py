from django.urls import path
from HAStudio import views

urlpatterns = [
    path('', views.index, name='index'),
    path('services', views.services, name='services'),
    # path('news', views.post_list, name='post_list'),
    path('news', views.PostListView.as_view(), name='post_list'),
    path('registration', views.registration, name='registration'),
    path('contacts', views.contacts, name='contacts'),
    path('about', views.about, name='about'),
    path('<slug:post>/', views.post_detail, name='post_detail'),
]
