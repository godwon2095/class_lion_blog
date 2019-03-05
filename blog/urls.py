from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('show/<int:blog_id>/', views.show, name="show"),
    path('create/', views.create, name="create"),
]