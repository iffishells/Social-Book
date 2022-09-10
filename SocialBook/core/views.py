from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect

# models
from .models import Profile, Post, LikePost, FollowerCount


# Create your views here.


@login_required(login_url='sign_in')
def index(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)

    # getting all the user option
    post = Post.objects.all()
    return render(request, 'index.html', {'user_profile': user_profile,
                                          'post': post})


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
                # lets redirect the setting for the user
                user_login = auth.authenticate(username=username, password=password1)
                auth.login(request, user_login)
                # lets add in current model for the profile model
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model,
                                                     id_user=user_model.id)
                new_profile.save()
                messages.info(request, 'Your account has Successfully created!')
                return redirect('/')
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


@login_required(login_url='sign_in')
def logout(request):
    return redirect('/SignIn')


@login_required(login_url='sign_in')
def setting(request):
    User_Profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':

        if request.FILES.get('image') is None:
            image = User_Profile.profile_img
            bio = request.POST.get('bio', False)
            location = request.POST.get('location', False)

            User_Profile.profile_img = image
            User_Profile.bio = bio
            User_Profile.location = location
            User_Profile.save()
        if request.FILES.get('image') != None:
            image = request.FILES.get('image')
            bio = request.POST['bio']
            location = request.POST['location']

            User_Profile.profile_img = image
            User_Profile.bio = bio
            User_Profile.location = location
            User_Profile.save()
        return redirect('/Setting')

    return render(request, 'setting.html', {'User_Profile': User_Profile})

@login_required(login_url='sign_in')
def upload(request):
    print(request)
    if request.method == 'POST':
        user = request.user.username
        caption = request.POST['caption']
        image = request.FILES.get('image_upload')
        print('---------------------------------------------------------------------------')
        user_profile_post = Post.objects.create(user=user, caption=caption, image=image)
        user_profile_post.save()
        return redirect('/')
    else:
        return redirect('/')

@login_required(login_url='sign_in')
def like_post(request):
    print('like post method request received')
    username = request.user.username
    post_id = request.GET.get('post_id')

    post = Post.objects.get(id=post_id)

    like_filter = LikePost.objects.filter(post_id=post_id, username=username).first()

    if like_filter is None:
        new_like = LikePost.objects.create(post_id=post_id, username=username)
        new_like.save()

        post.no_of_like = post.no_of_like + 1
        post.save()
        return redirect('/')
    else:
        like_filter.delete()
        post.no_of_like = post.no_of_like - 1
        post.save()
        return redirect('/')

@login_required(login_url='sign_in')
def profile(request, pk):
    user_object = User.objects.get(username=pk)
    user_profile = Profile.objects.get(user=user_object)
    user_post = Post.objects.filter(user=pk)

    user_follower = request.user.username
    user = pk
    if FollowerCount.objects.filter(follower = user_follower,username=user).first():
        button_text = 'Unfollow'
    else:
        button_text = 'Following'
    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'user_post': user_post,
        'user_post_len': len(user_post),
        'button_text':button_text
    }
    return render(request, 'profile.html', context)

@login_required(login_url='sign_in')
def follower(request):
    if request.method is 'POST':
        user_follower = request.POST['follower']
        user = request.POST['user']
        print(f' follower {user_follower} and user {user}')

        if FollowerCount.objects.filter(follower=user_follower, user=user).first():
            delete_follower = FollowerCount.objects.get(follower=user_follower, user=user)
            delete_follower.delete()
            return redirect('/profile/' + user)
        else:
            new_follower = FollowerCount.objects.create(follower=user_follower, user=user)
            new_follower.save()
            return redirect('/profile/' + user)
    else:
        return redirect('/')
