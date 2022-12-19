from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.views import  View

def index(request):
    return render(request, 'index.html')








#class Cart(View):
  #  def get(self, request):
      #  products = Product.get_products_by_name(names)
       # print(products)
        #return render(request, 'cart.html', {'products': products})



def add_cart(request):
    products = Product.objects.all
    Toggle = ''
    addcart = ''

    Toggle = request.get['toggle']
    if Toggle == 'true':
           addcart += products.name
    return addcart

def cart(request):
    addcart = ' '
    tick =request.POST.get("toggle")

    return render(request, 'cart.html',{'tick':tick} )



def grocery(request):
    products = Product.objects.all
    return render(request, 'groceries.html', {'products': products})



