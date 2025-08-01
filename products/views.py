from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from.models import Category, Product


def index(request):
  return HttpResponse("This is Product Page")

def products(request):
  all_products = Product.objects.all()
  return render(request, 'products/products1.html', {'products': all_products})

def product_detail(request, id):
  product = get_object_or_404(Product, id=id)
  return render(request, 'products/details1.html', {'product':product})

