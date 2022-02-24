from pickle import FALSE, TRUE
from tkinter import Image
from tokenize import Name
from django.db import models

class cake(models.Model):
    Name = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='pics')
    Price = models.IntegerField()
    Stock = models.FloatField()
    Date = models.DateTimeField(auto_now_add=True)
    Desc=models.TextField()
    Offer = models.FloatField()
    Offer2 = models.BooleanField(default=False)
