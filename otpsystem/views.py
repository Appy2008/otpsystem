import imp
from django.shortcuts import redirect, render
from .models import *
import random

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        profile = Profile.objects.filter(email = email)
        if not profile.exists():
            return redirect('/register/')
        profile[0].otp = random.randint(1000,9999)
        profile[0].save()
        print(profile[0].otp)

        return redirect(f'/otp/{profile[0].uid}')

def register_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.create(email = email)
        profile = Profile.objects.create(user=user, email=email)

        return redirect('/')
    
    return render(request,'register.html')

def dashboard_view(request):
    return render(request,'dashboard.html')

def otp(request,uid):
    return render(request,'otp.html')