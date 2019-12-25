
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.welcome),
    path("wish/", views.wish),
    path("greet/", views.greet),
    path("books/", views.list_books),
    path("addbook/", views.add_book),
]
