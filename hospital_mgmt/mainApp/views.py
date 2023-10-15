from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

def home(request):
    return render(request,"index.html")

def login_user(request):
    return render(request,"login.html")


def signup(request):
    if (request.method=="POST"):
        drop = str(request.POST.get("category"))
        if drop == "patient":
            pas = request.POST.get("password")
            cpass = request.POST.get("cpassword")
            if (pas==cpass):
                pat = patient()
                pat.fname = request.POST.get("fname") 
                pat.lname = request.POST.get("lname") 
                pat.username = request.POST.get("username") 
                pat.email = request.POST.get("email") 
                pat.address1 = request.POST.get("address1") 
                pat.state = request.POST.get("state") 
                pat.city = request.POST.get("city") 
                pat.pincode = request.POST.get("pincode") 
                pat.pic=request.FILES.get("profile")
                useR = User (username=pat.username,email=pat.email,password=pas)
                useR.set_password(pas)
                useR.save()
                pat.save()
                return redirect("/")
            else:
                messages.error(request,"Password does not match")
        elif drop == "doctor":
            pas1 = request.POST.get("password")
            cpass = request.POST.get("cpassword")
            if (pas1==cpass):
                doc = doctor()
                doc.fname = request.POST.get("fname") 
                doc.lname = request.POST.get("lname") 
                doc.username = request.POST.get("username") 
                doc.email = request.POST.get("email") 
                doc.address1 = request.POST.get("address1") 
                doc.state = request.POST.get("state") 
                doc.city = request.POST.get("city") 
                doc.pincode = request.POST.get("pincode") 
                doc.pic = request.FILES.get("profile")
                useR = User (username=doc.username,email=doc.email,password=pas1)
                useR.set_password(pas1)
                useR.save()
                doc.save()
                return redirect("/")
            else:
                messages.error(request,"Password does not match")
        else:
            messages.error(request,"Select User type and retry")
    return render(request,"signup.html")

def patient_login(request):
    if (request.method=="POST"):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)
        if (user is not None):
            login(request,user)
            if(user.is_superuser):
                return redirect("/admin/")
            else:
                return redirect("/pat_dashboard/")
    return render(request,"cust_login.html")

def pat_dashboard(request):
    user = User.objects.get(username=request.user)
    if(user.is_superuser):
        return redirect("/admin/")
    else:
        pat = patient.objects.get(username=user.username)
    return render(request,"pat_dashboard.html",{"pat":pat})

def doctor_login(request):
    if (request.method=="POST"):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)
        if (user is not None):
            login(request,user)
            if(user.is_superuser):
                return redirect("/admin/")
            else:
                return redirect("/doc_dashboard/")
    return render(request,"doc_login.html")

def doc_dashboard(request):
    user = User.objects.get(username=request.user)
    if(user.is_superuser):
        return redirect("/admin/")
    else:
        doc = doctor.objects.get(username=user.username)
    return render(request,"doc_dashboard.html",{"doc":doc})

def logout_page(request):
    logout(request)
    return redirect("/")

def contactPage(request):
    if (request.method=="POST"):
        c = contactUs()
        c.name = request.POST.get("name")
        c.email = request.POST.get("email")
        c.message = request.POST.get("message")
        c.save()
        messages.success(request,"Thanks for Contacting us!!! We will get in touch soon!!")
    return render(request,"contact.html")


def aboutus(request):
    return render(request,"about.html")

