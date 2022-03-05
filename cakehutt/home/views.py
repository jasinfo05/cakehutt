from django.shortcuts import render
from django.http import HttpResponse
from . models import cake

'''product1 = cake()
product1.Name = 'Choco-Almond Fusion'
product1.Price = 300
product1.Image = 'Choco-Almond Fusion.jpg'

product2 = cake()
product2.Name = 'Berry Delight'
product2.Price = 245
product2.Image = 'Berry Delight.jpg'

product3 = cake()
product3.Name = 'Coco-Sphere'
product3.Price = 280
product3.Image = 'Coco-Sphere.jpg'

product4 = cake()
product4.Name = 'Strawberry Zaakki'
product4.Price = 250
product4.Image = 'Strawberry Zaakki.jpg'''


def index(request):
    product= cake.objects.all()
    return render(request,'index_2.html',{'Pro': product})
    
