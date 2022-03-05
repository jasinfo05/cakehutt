from itertools import product
from django.shortcuts import redirect, render
from home.models import cake
from django.core.cache import cache

def details(request):
    ID=request.GET['id']
    product=cake.objects.get(id=ID)
    off=product.Price*product.Offer/100
    offerprice=product.Price-off
    
    return render(request,'single-product.html',{'pro':product,'ofr':offerprice})

    
    


