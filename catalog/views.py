from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
import sqlite3


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


def greet(request):
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

    return render(request,'greet.html',
                  {'name' : name, 'message' : msg})

def list_books(request):
    con = sqlite3.connect(r"e:\classroom\python\dec2\books_catalog.db")
    cur = con.cursor()
    cur.execute("select * from books")
    books = cur.fetchall()
    con.close()
    return render(request,'list_books.html', {'books' : books})


def add_book(request):
    if request.method == "GET" :   # GET request
        return render(request,'add_book.html')
    else:  # POST request with data after submit
        title = request.POST['title']
        publisher = request.POST['publisher']
        authors = request.POST['authors']
        price = request.POST['price']
        try:
            con = sqlite3.connect(r"e:\classroom\python\dec2\books_catalog.db")
            cur = con.cursor()
            cur.execute("insert into books(title,publisher,authors,price) values(?,?,?,?)",
                    (title,publisher,authors,price))
            con.commit()
            con.close()
            return redirect("/catalog/books")
        except Exception as ex:
            print("Error during adding book ", ex)
            return render(request, 'add_book.html',{'message': 'Sorry! Could not add book!'})

