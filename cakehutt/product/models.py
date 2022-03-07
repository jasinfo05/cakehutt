from django.db import models
from home.models import cake

class comment(models.Model):
    cakes=models.ForeignKey(cake,related_name="comments",on_delete=models.CASCADE)
    Name=models.CharField(max_length=100)
    Message=models.TextField()
    Date=models.DateTimeField(auto_now_add=True)

