from django.contrib import admin
from django.urls import path,include
from mysite import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.url')),
    path('category',include('category.url')),
    path('about',include('about.url')),
    path('login',include('login.url')),
    path('Register',include('Register.url')),
    path('contact',include('contact.url')),
]
