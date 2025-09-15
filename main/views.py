from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from main.models import Product

def show_main(request):
    context = {
        'npm': '2406404913',
        'name': 'Zita Nayra Ardini',
        'class' : 'PBP F'
    }

    return render(request, "main.html", context)

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
