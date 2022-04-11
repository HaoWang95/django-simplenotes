from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home.index'),
    path('home/authorized', views.AuthorizedView.as_view()),
    path('login', views.LoginInterfaceView.as_view(), name='home.login'),
    path('logout', views.LogoutInterfaceView.as_view(), name='home.logout'),
    path('register', views.SignupView.as_view(), name='home.register'),
    path('passwordchange', views.PasswordChangeInterfaceView.as_view(), name='home.passwordchange')
]