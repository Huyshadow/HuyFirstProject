from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

from .models import Feature

def index(request):
    feature_list = Feature.objects.all()
    return render(request,'index.html', {'feature_list':feature_list}) # Truyen parameter de no dinamic
    # chi truyen duoc voi dictionary
# Create your views here.

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re_password']

        if password == re_password:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Exists')
                return redirect('register')
            elif User.objects .filter(username= username).exists():
                messages.info(request, "Username Already Exist")
                return redirect('register')
            else:
                user = User.objects.create_user(username = username, email = email, password = password)
                user.save();
                return redirect('login')
        else: 
            messages.info(request, 'Password Not the same')
            return redirect('register')
    else: 
        return render(request,'register.html',)

def counter(request):
    text = request.POST['text']
    nums_of_word = len(text.split())
    return render(request,'counter.html',{'nums_of_word': nums_of_word}) 
