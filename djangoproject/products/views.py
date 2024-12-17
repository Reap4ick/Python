from django.http import HttpResponse
from django.shortcuts import render

from products.models import Product



# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})
def list(request):
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})



def details(request, id):
    try:
        product = Product.objects.get(pk=id)
        print(product)
        return render(request, "detail.html", {"product": product})
        
    except:
        error="Product not except"
        return render(request, "detail.html", {"error": error})
    
    # return render(request, "detail.html", {"product": product, "error": error})