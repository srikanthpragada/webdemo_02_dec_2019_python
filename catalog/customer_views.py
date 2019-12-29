from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.db.models import Count
from .models import Customer
from django.core.exceptions import ObjectDoesNotExist
from .forms import CustomerForm


def customer_home(request):
    summary = Customer.objects.all().aggregate(count=Count('id'))
    return render(request, 'customer_home.html',
                  {'summary': summary})


def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html',
                  {'customers': customers})


def customer_delete(request, id):
    try:
        cust = Customer.objects.get(id=id)
        cust.delete()
        return redirect("/catalog/customer/list")
    except ObjectDoesNotExist:
        return render(request, 'customer_delete.html',
                      {'msg': 'Customer Id Not Found!'})
    except:
        return render(request, 'customer_delete.html',
                      {'msg': 'Customer could not be deleted!'})


def customer_add(request):
    if request.method == "GET":
        form = CustomerForm()
        return render(request, 'customer_add.html',
                      {'form': form})
    else:  # POST
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()  # Add customer to table
            return redirect("/catalog/customer/list")
        else:
            return render(request, 'customer_add.html',
                          {'form': form})


#
def customer_edit(request, id):
    if request.method == "GET":
        try:
            cust = Customer.objects.get(id=id)
            form = CustomerForm(instance=cust)
            return render(request, 'customer_edit.html',
                          {'form': form})
        except ObjectDoesNotExist:
            return render(request, 'customer_edit.html',
                          {'msg': 'Customer Id Not Found!'})
    else:
        author = Customer.objects.get(id=id)
        form = CustomerForm(instance=author, data=request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'customer_edit.html',
                          {'form': form})
        return redirect("/catalog/customer/list")


def validate_email(request):
    try:
        email = request.GET['email']
        cust = Customer.objects.get(email=email)
        return HttpResponse("p")  # Email is present
    except ObjectDoesNotExist:
        return HttpResponse("u")  # Email is not present, means unique


#
#
def customer_search(request):
    return render(request, 'customer_search.html')


def customer_do_search(request):
    name = request.GET['name']
    # convert author objects to dict
    customers = list(Customer.objects.filter(name__contains=name).values())
    # send list of dict in the form of array of json objects
    return JsonResponse(customers, safe=False)
