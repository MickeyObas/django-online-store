from django.shortcuts import render
from .models import Category, Product
from django.shortcuts import get_object_or_404
from django.db.models import Q


def product_all(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    products = Product.objects.filter(Q(category__name__icontains=q) | Q(title__icontains=q) | Q(description__icontains=q))
    return render(request, 'store/index.html', {'products':products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/product_detail.html', {'product':product})

def category_list(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/category.html', {'products':products, 'category':category})

