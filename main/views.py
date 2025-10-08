from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from main.models import Product
from main.forms import ProductForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)
    
    context = {
        'npm': '2406404913',
        'name': request.user.username,
        'class' : 'PBP F',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)


def create_product(request):
    form = ProductForm(request.POST or None)
    
    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit= False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')
    
    context = {
        'form': form
    }
    
    return render(request, 'create_product.html', context)

# Menambahkan Product dengan AJAX
@csrf_exempt
@require_POST
def create_product_ajax(request):
    name = request.POST.get("name")
    price = request.POST.get("price")
    description = request.POST.get("description")
    thumbnail = request.POST.get("thumbnail")
    rating = request.POST.get("rating")
    category = request.POST.get("category")
    is_discount = request.POST.get("is_discount") == 'on'
    brand = request.POST.get("brand")
    user = request.user

    product = Product(
        name=name,
        price=price,
        description=description,
        thumbnail=thumbnail,
        rating=rating,
        category=category,
        is_discount=is_discount,
        brand=brand,
        user=user,
    )
    product.save()

    return HttpResponse(b"CREATED", status=201)

@login_required(login_url='/login')
def show_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = { 'product': product }
    return render(request, 'show_product.html', context)
        
def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

# Menampilkan data dalam format JSON AJAX
def show_json(request):
    product_list = Product.objects.all()
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.get_category_display(),
            'is_discount': product.is_discount,
            'brand': product.brand,
            'rating': product.rating,
            'user_id': product.user.id if product.user else None,
        }
        for product in product_list
    ]
    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
    try:
        product = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)
    
# Menampilkan data dalam format JSON berdasarkan ID dengan AJAX
def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail if product.thumbnail else None,
            'category': product.get_category_display(),
            'is_discount': product.is_discount,
            'rating': float(product.rating) if product.rating is not None else 0,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
    
@csrf_exempt  # Hanya untuk AJAX POST, pastikan CSRF token dikirim dari client
def register(request):
    form = UserCreationForm()
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'message': 'Your account has been successfully created!',
                    'redirect': '/login/'  # URL untuk redirect setelah sukses
                })
            messages.success(request, 'Your account has been successfully created')
            return redirect('main:login')
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                errors = form.errors.as_json()
                return JsonResponse({
                    'success': False,
                    'message': 'Registration failed.',
                    'errors': errors
                }, status=400)
    
    context = {'form': form}
    return render(request, 'register.html', context)

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            last_login = str(datetime.datetime.now())
            
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                response = JsonResponse({
                    'success': True,
                    'message': 'Welcome back! Redirecting to homepage...',
                    'redirect': reverse('main:show_main')
                })
                response.set_cookie('last_login', last_login)
                return response
            else:
                response = HttpResponseRedirect(reverse("main:show_main"))
                response.set_cookie('last_login', last_login)
                return response
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                errors = form.errors.as_json()
                return JsonResponse({
                    'success': False,
                    'message': 'Invalid username or password.',
                    'errors': errors
                }, status=400)
    
    form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)


@csrf_exempt
def logout_user(request):
    logout(request)
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        response = JsonResponse({
            'success': True,
            'message': 'You have been logged out successfully.',
            'redirect': reverse('main:login')
        })
        response.delete_cookie('last_login')
        return response
    else:
        response = HttpResponseRedirect(reverse('main:login'))
        response.delete_cookie('last_login')
        return response

from .forms import ProductForm

@csrf_exempt
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)

    if request.method == "GET":
        data = {
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "description": product.description,
            "thumbnail": product.thumbnail,
            "rating": product.rating,
            "category": product.category,
            "is_discount": product.is_discount,
            "brand": product.brand,
        }
        return JsonResponse(data)

    elif request.method == "POST":
        product.name = request.POST.get("name")
        product.price = request.POST.get("price")
        product.description = request.POST.get("description")
        product.thumbnail = request.POST.get("thumbnail")
        product.rating = request.POST.get("rating")
        product.category = request.POST.get("category")
        product.is_discount = request.POST.get("is_discount") == "on"
        product.brand = request.POST.get("brand")
        product.save()

        return JsonResponse({"success": True})

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse("main:show_main"))

# Menghapus Product dengan AJAX
@require_POST
def delete_product_ajax(request, id):
    try:
        product = get_object_or_404(Product, pk=id)
        product.delete()
        return JsonResponse({"success": True, "message": "Product deleted successfully!"})
    except Exception as e:
        return JsonResponse({"success": False, "message": str(e)})


