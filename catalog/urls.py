
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.welcome),
    path("wish/", views.wish),
    path("greet/", views.greet),
    path("books/", views.list_books),
    path("addbook/", views.add_book),
    path("addbook2/", views.add_book2),
    path("countries/", views.list_countries),
]
