from django.shortcuts import render
from django.core.serializers import deserialize
from .models import Product

def index(request):
    with open('myapp/fixtures/products.json', 'r') as f:
        data = list(deserialize('json', f))
        products = [item.object for item in data]
    return render(request, 'index.html', {'products': products})

def show(request, id):
    with open('myapp/fixtures/products.json', 'r') as f:
        data = list(deserialize('json', f))
        product = next((item.object for item in data if item.object.pk == id), None)
    return render(request, 'show.html', {'product': product})

