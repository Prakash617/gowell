"""
URL configuration for gowell project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name = 'home'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('blog-grid/', blog_grid, name='blog-grid'),
    path('blog-detail/', blog_detail, name='blog-detail'),
    path('pricing/', pricing, name='pricing'),
    path('features/', features, name='features'),
    path('team/', team, name='team'),
    path('testimonials/', testimonials, name='testimonials'),
    path('quote/', quote, name='quote'),
    path('contact/', contact, name='contact'),
]
