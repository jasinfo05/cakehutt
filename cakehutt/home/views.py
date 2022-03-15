from django.shortcuts import render
from django.http import HttpResponse
from . models import cake

def index(request):
    product= cake.objects.all()
    #cookies viewing
    if 'email' in request.COOKIES and 'prod_name' in request.COOKIES:
        jinjatext={
            'Pro':product,
            'Name':request.COOKIES['name'],
            'Email':request.COOKIES['email'],
            'Number':request.COOKIES['number'],
            
        }
        return render(request,'index_2.html',jinjatext)

    else:
        return render(request,'index_2.html',{'Pro': product})
    
