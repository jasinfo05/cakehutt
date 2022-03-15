from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User,auth

def login1(request):
    if request.method == 'POST':
        uname = request.POST['Uname']
        pname = request.POST['Pname']
        user = auth.authenticate(username=uname,password=pname)
        if user is not None:
            obj=User.objects.get(username=user)
        #cookies setting
            print(obj.first_name)
            print(obj.email)
            print("hai",user.first_name)
            auth.login(request,user)
            response=redirect('/')
            response.set_cookie("name",user.first_name)
            response.set_cookie("email",user.email)
            response.set_cookie("number","123456")
            return response
            
        else:
            lmsg="Incorrect username or password!"
            return render(request,'login.html',{'Lmsg':lmsg})
    else:
        #this works on get method
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    response=redirect('/')

    #cookies deleting

    response.delete_cookie("name")
    response.delete_cookie("email")
    response.delete_cookie("number")
    return response

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
                auth.login(request,user)
                return redirect('/')
        else:
            pmsg="Password is not matching!"
            return render(request,'register.html',{'Pmsg':pmsg})
    else:
        #this works on GET method
        return render(request,'register.html')


    


