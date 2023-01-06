# from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.RadioView.as_view(), name="SpamHome"),
    path('index.html/', views.RadioView.as_view(), name="index"),
    path('about.html/', views.about, name="about"),
]
