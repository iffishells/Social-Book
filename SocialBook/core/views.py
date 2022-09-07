from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect

from .models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='sign_in')
def index(request):
    return render(request, 'index.html')


def sign_up(request):
    if request.method == 'POST':

        username = request.POST['Username']
        email = request.POST['email']
        password1 = request.POST['Password1']
        password2 = request.POST['Password2']
        # if post request come here then we need to collect the data

        # check if email already exist
        # if User.objects.filter(email=email):

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Taken')
                return redirect('sign_up')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'UserName Already Taken')
                return redirect('sign_up')
            else:
                user = User.objects.create_user(email=email,
                                                username=username,
                                                password=password1)
                user.save()
                # lets add in current model for the profile model
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model,
                                                         id_user =user_model.id)
                new_profile.save()
                messages.info(request,'Your account has Successfully created!')
                return redirect('sign_up')
        else:
            messages.info(request, 'Passwords are not match')
            return redirect('sign_up')

    else:
        return render(request, 'signup.html')

def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials are not Valid')
            return redirect('sign_in')

    return render(request, 'signin.html')


@login_required(login_url='SignIn')
def logout(request):
    return redirect('/SignIn')
