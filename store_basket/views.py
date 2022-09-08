from django.shortcuts import render, get_object_or_404, HttpResponse
from .basket import Basket

from django.http import JsonResponse
from store.models import Product

# Create your views here.
def basket_summary(request):
    basket = Basket(request)
    return render(request, 'store_basket/index.html', {"basket":basket})

def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        quantity = int(request.POST.get('quantity'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, quantity=quantity)

        basket_quantity = basket.__len__()
        response = JsonResponse({'quantity': basket_quantity})

        print(basket.basket)
        print(basket.basket.keys())
        print(basket.basket.values())
        
        return response

def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        basket.delete(product=product_id)
        basket_qty = basket.__len__()
        basket_total = basket.get_total_price()
        response = JsonResponse({'subtotal':basket_total, 'qty':basket_qty})
        return response

def basket_update(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_quantity = int(request.POST.get('productquantity'))
        basket.update(product=product_id, product_quantity=product_quantity)

        basket_qty = basket.__len__()
        basket_total = basket.get_total_price()
        
        response = JsonResponse({'qty':basket_qty, 'subtotal':basket_total})
        return response


