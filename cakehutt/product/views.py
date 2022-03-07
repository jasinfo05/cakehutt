from itertools import product
from django.shortcuts import redirect, render
from home.models import cake
from django.core.cache import cache

def details(request):
    ID=request.GET['id']
    if cache.get(ID):
        print("DATA FROM CACHE")
        product=cache.get(ID)
        off=product.Price*product.Offer/100
        offerprice=product.Price-off
    
    else:
        product=cake.objects.get(id=ID)
        cache.set(ID,product)
        print("DATA FROM DATABASE")
        off=product.Price*product.Offer/100
        offerprice=product.Price-off
    return render(request,'single-product.html',{'pro':product,'ofr':offerprice})

    
    


