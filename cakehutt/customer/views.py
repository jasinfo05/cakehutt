from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User,auth

def login1(request):
    if request.method == 'POST':
        uname = request.POST['Uname']
        pname = request.POST['Pname']
        user = auth.authenticate(username=uname,password=pname)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            lmsg="Incorrect username or password!"
            return render(request,'login.html',{'Lmsg':lmsg})
    else:
        #this works on get method
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def register1(request):
    if request.method == 'POST':
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
    else:
        #this works on GET method
        return render(request,'register.html')


    


