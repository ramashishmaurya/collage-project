from django.shortcuts import render , redirect , HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.


def signup(requests):
    if requests.method =='POST':
        email = requests.POST['email']
        password = requests.POST['pass1']
        confirm_password = requests.POST['pass2']
        if password != confirm_password:
            messages.warning(requests , "password is not matching")
            return render (requests ,"signup.html")
        try:
            if User.objects.get(username=email):
                return HttpResponse("Email Already exist")
            
        except Exception as IndentationError: #use == username ckeck again 
            pass
        user = User.objects.create_user(email,email,password)
        user.save()
        return HttpResponse("USer created" , email)
    return render(requests , "authentication/signup.html")



def signup(requests):
    return render(requests ,'authentication/signup.html')


def blog(requests):
    return HttpResponse("this is the blog page ")



def handlelogin(requests):
    return render(requests,'authentication/login.html')

def handlelogout(requests):
    return redirect('/auth/login')

