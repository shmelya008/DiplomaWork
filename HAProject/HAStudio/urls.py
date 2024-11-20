from django.urls import path
from HAStudio import views


urlpatterns = [
    path('login', views.user_login, name='login'),
    path('logout', views.logout, name='logout'),
    path('services', views.services, name='services'),
    path('contacts', views.contacts, name='contacts'),
    path('about', views.about, name='about'),
    path('posts', views.PostListView.as_view(), name='post_list'),
    path('<slug:slug>', views.PostDetailView.as_view(), name='post_detail'),
    path('', views.index, name='index'),
]


# path('login/', views.user_login, name='login'),
# path('logout', views.logout, name='logout'),
# path('logout', 'django.contrib.auth.views.logout', name='logout'),
# path('login', 'django.contrib.auth.views.login', name='login'),
# path('logout-then-login', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),