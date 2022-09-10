from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Signup', views.sign_up, name='sign_up'),
    path('SignIn', views.sign_in, name='sign_in'),
    path('Logout', views.logout, name='logout'),
    path('Setting', views.setting, name='setting'),
    path('upload', views.upload, name='upload'),
    path('like-post', views.like_post, name='like_post'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('follower', views.follower, name='follower')
]
