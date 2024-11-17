from django.urls import path
from HAStudio import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('services', views.services, name='services'),
    # path('news', views.post_list, name='post_list'),
    # path('<slug:post>/', views.post_detail, name='post_detail'),
]
