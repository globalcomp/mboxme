from django.urls import path, re_path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path("contact", views.contact, name="contact"),
    path('about', views.about, name='about'),
    path('profile/home', views.home, name='home'),
]