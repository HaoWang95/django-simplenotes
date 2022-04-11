from datetime import datetime
from typing import Any
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
# Create your views here.

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = '/notes'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request, *args, **kwargs)


class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'


class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'


class PasswordChangeInterfaceView(PasswordChangeView):
    template_name = 'home/password_change.html'
    success_url = '/'


class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}

def home(request):
    print(request)
    return render(request, 'home/welcome.html', {
        'today':datetime.today()
    })


class AuthorizedView(TemplateView, LoginRequiredMixin):
    template_name = 'home/authorized.html'
    login_url = '/admin'


@login_required(login_url='/admin')
def authorized(request):
    return render(request, 'home/authorized.html', {})