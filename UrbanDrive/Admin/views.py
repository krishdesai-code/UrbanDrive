from django.shortcuts import render,redirect
from .models import Admin_login

def admin_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("pass")

        try :
            admin = Admin_login.objects.get(email=email)

            if admin.password == password :
                request.session['email'] = admin.email
                return redirect('admin_home')
            else :
                error = "Invalid Email Id or password"
        
        except Admin_login.DoesNotExist:
            error = "Invalid Email Id or password"
        return render(request,"admin/login.html",{'error' : error})
    return render(request,"admin/login.html")

def admin_home(request):
    return render(request,'admin/home.html')