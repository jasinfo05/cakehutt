from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login,name='loginpage'),
    path('register/',views.register,name='registerpage'),
    path('register/register2/',views.register2,name='register2page'),
    path('login/login1',views.login1,name='login1page')
    
]