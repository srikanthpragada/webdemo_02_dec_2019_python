
from django.contrib import admin
from django.urls import path
from . import views, customer_views

urlpatterns = [
    path('welcome/', views.welcome),
    path("wish/", views.wish),
    path("greet/", views.greet),
    path("books/", views.list_books),
    path("addbook/", views.add_book),
    path("addbook2/", views.add_book2),
    path("countries/", views.list_countries),
    path("customer/home/", customer_views.customer_home),
    path("customer/list/", customer_views.customer_list),
    path("customer/add/", customer_views.customer_add),
    path("customer/delete/<int:id>/", customer_views.customer_delete),
    path("customer/edit/<int:id>/", customer_views.customer_edit),
]
