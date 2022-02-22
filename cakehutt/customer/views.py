from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User,auth

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def register2(request):
    uname = request.POST['Uname']
    fname = request.POST['Fname']
    lname = request.POST['Lname']
    ename = request.POST['Ename']
    pname = request.POST['Pname']
    repname = request.POST['Repname']
    if pname == repname:
        if User.objects.filter(username = uname).exists():
            umsg="Username is taken!"
            return render(request,'register.html',{'Umsg':umsg})
        elif User.objects.filter(email = ename).exists():
            emsg="Email is taken!"
            return render(request,'register.html',{'Emsg':emsg})
        else:
            user=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=ename,password=pname)
            user.save();
            return render(request,'success.html')

    else:
        pmsg="Password is not matching!"
        return render(request,'register.html',{'Pmsg':pmsg})

def login1(request):
    uname = request.POST['Uname']
    pname = request.POST['Pname']
    user = auth.authenticate(username=uname,password=pname)
    if user is not None:
        auth.login(request,user)
        return redirect('/')
    else:
        return render(request,'login.html')
