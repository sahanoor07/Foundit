from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request,'index.html')
    
def category(request):
    return HttpResponse("Welcome to the web page")

def about(request):
    return HttpResponse("Welcome to the web page")

def login(request):
    return render(request,'login.html')

def Register(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return render(request, 'register.html')
        
        my_user=User.objects.create_user(uname,email,pass1)
        my_user.save()
        return render(request,'login.html')
        print(uname,email,pass1,pass2)
    return render(request,'register.html')

def contact(request):
    return HttpResponse("Welcome to the web page")