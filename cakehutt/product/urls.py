from django.urls import path
from . import views

urlpatterns = [
    
    path('details/',views.details,name='details'),
    path('details/coment/',views.details,name='comments')
]