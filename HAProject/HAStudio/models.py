from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

# class User(models.Model):
#     name = models.CharField(max_length=120, null=False)
#     phone_number = models.CharField(max_length=15, null=False)
#     email = models.EmailField()
#     required_service = models.CharField(max_length=20, null=False)
#     balance = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
#     objects = models.Manager()
#     DoesNotExist = models.Manager
#
#     def __str__(self):
#         return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    birth_date = models.DateField(null=True, blank=True)
    requested_service = models.CharField(max_length=20, null=False)
    balance = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    objects = models.Manager()
    DoesNotExist = models.Manager


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    body = models.TextField()
    file = models.FileField(upload_to='files', verbose_name='Texts file', null=True, blank=True)
    image = models.ImageField(upload_to='images', verbose_name='Media file', null=True, blank=True)
    publish = models.DateField(default=timezone.now())
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    objects = models.Manager()
    DoesNotExist = models.Manager

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
