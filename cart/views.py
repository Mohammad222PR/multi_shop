from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from product.models import Product
from .utils import Cart
# Create your views here.


class CartDetailView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request,'cart/cart_deatil.html', {'cart':cart})
    

class CartAddView(View):
    def post(self, request, pk):
        product = get_object_or_404(Product,id = pk)
        size, color, quantity = request.POST.get('size', 'empty'), request.POST.get('color', 'empty'), request.POST.get('quantity')
        cart = Cart(request)
        cart.add(product, int(quantity), color, size)
        return redirect('cart:cart_detail')
    

class ItemDeletView(View):
    def get(self, request, id):
        cart = Cart(request)
        cart.delete(id)
        return redirect('cart:cart_detail')