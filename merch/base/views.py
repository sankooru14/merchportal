from django.shortcuts import render,redirect
# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from api.serializers import MerchSerializer,OrderSerializer
from .models import Merch,Order
import requests
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import Http404
from .forms import AddOrderForm
from django.contrib import messages
# Create your views here.
       
def merch_list(request):
    allMerch = Merch.objects.filter(size='S')
    return  render ( request , 'base/merch_list.html',{'allMerch':allMerch})

def merch_detail(request,size_key,name):
    merch = get_object_or_404(Merch,size=size_key,name=name)
    return  render ( request , 'base/merch_detail.html',{'merch':merch})

def add_order(request,pk):
    merch = get_object_or_404(Merch,id=pk)
    if request.method == 'POST':
        form = AddOrderForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            room_no = form.cleaned_data['room_no']
            hostel = form.cleaned_data['hostel']
            quantity = form.cleaned_data['quantity']
            order = Order(name=name, email=email, room_no=room_no, hostel=hostel,quantity=quantity,merch = merch)
            order.save()
            print(order.id)
            messages.success(request, 'Form submission successful')
            print(form.cleaned_data)
            return order_detail(request,order.id)
    else:
        form = AddOrderForm()
    return  render ( request , 'base/add_order.html',{'merch':merch,'form':form})

def order_detail(request,pk):
    order = get_object_or_404(Order,id=pk)
    return  render ( request , 'base/order_detail.html',{'order':order})


