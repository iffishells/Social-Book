from django.shortcuts import render,redirect

from .models import Profile
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'index.html')

def sign_up(request):
    if request.method =='POST':

        username = request.POST['Username']
        email = request.POST['email']
        password1 = request.POST['Password1']
        password2 = request.POST['Password2']
        # if post request come here then we need to collect the data

        # check if email already exist
        # if User.objects.filter(email=email):

        if password1 == password2:
            pass
        else:
            messages.info(request,'Passwords are not match')
            return redirect('signup')


    else:
        return render(request, 'signup.html')
