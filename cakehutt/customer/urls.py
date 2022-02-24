from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login1,name='loginpage'),
    path('register/',views.register1,name='registerpage'),
    path('logout/',views.logout,name='logoutpage')
]