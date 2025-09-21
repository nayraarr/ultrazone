from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from main.models import Product
from main.forms import ProductForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def show_main(request):
    product_list = Product.objects.all()
    
    context = {
        'npm': '2406404913',
        'name': 'Zita Nayra Ardini',
        'class' : 'PBP F',
        'product_list': product_list
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)
    
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')
    
    context = {
        'form': form
    }
    
    return render(request, 'create_product.html', context)

def show_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = { 'product': product }
    return render(request, 'show_product.html', context)
        
def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    json_data = serializers.serialize("json", product_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, product_id):
    try:
        product = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)
    
def show_json_by_id(request, product_id):
    try:
        product = Product.objects.filter(pk=product_id)
        json_data = serializers.serialize("json", product)
        return HttpResponse(json_data, content_type="application/json")
    except Product.DoesNotExist:
        return HttpResponse(status=404)
    
def register(request):
    form = UserCreationForm()
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created')
            return redirect('main:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        
        if form.is_valid():
            user = form.get_user
            login(request, user)
            return redirect('main:show_main')
    
    else:
        form = AuthenticationForm(request)
    
    context = {'form':form}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    return redirect('main:login')



