from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


# Create your views here.

def welcome(request):
    return HttpResponse("<h1>Welcome To Catalog Application</h1>")


def wish(request):
    hours = datetime.now().hour
    if 'user' in request.GET:
        name = request.GET['user']
    else:
        name = "Guest"

    if hours < 12:
        msg = "Good Morning"
    elif hours < 16:
        msg = 'Good Afternoon'
    else:
        msg = 'Good Evening'

    return HttpResponse(f"<h1 style='color:blue'>{msg} {name}</h1>")
