from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from catalog.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'email', 'mobile','profile')


@api_view(['GET', 'POST'])
def process_Customers(request):
    if request.method == "GET":
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)
    else:  # Post
        customer = CustomerSerializer(data=request.data)
        if customer.is_valid():
            customer.save()  # insert into table
            return Response(customer.data)
        else:
            return Response(customer.errors, status=400)  # bad request


@api_view(['GET', 'DELETE'])
def process_Customer(request, id):
    try:
        customer = Customer.objects.get(id=id)
    except:
        return Response(status=404)  # not found

    if request.method == "GET":
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    else:  # DELETE
        customer.delete()
        return Response(status=204)  # No data
