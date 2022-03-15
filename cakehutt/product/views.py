from audioop import reverse
from itertools import product
from queue import Empty
from django.shortcuts import redirect, render
from home.models import cake
from django.core.cache import cache
from . models import comment

def details(request):
    if request.method== 'POST':
        cmnt=request.POST['cmt']
        fnam=request.POST['Uname']
        pid=request.POST['Id']
        comt=comment.objects.create(cakes_id=pid,Name=fnam,Message=cmnt)
        comt.save();

        #page loading values
        product=cake.objects.get(id=pid)
        off=product.Price*product.Offer/100
        offerprice=product.Price-off

        return render(request,'single-product.html',{'pro':product,'ofr':offerprice})
    else:
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

    
        
        



    


