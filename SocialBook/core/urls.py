from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Signup', views.sign_up, name='sign_up')
]
