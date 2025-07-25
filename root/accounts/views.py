from django.shortcuts import render, HttpResponse, redirect
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def main(request):
    return HttpResponse('accounts')


def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(username=cd['username'], email=cd['email'], password=cd['password'])
            user.save()
            messages.success(request, 'registeration user is successfuly', 'success')
            return redirect('home:main')
    else:
        form = UserRegistrationForm(request.POST)
    return render(request, 'accounts/register.html', {'form':form})


def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'logged is successfuly', 'success')
                return redirect('home:main')
            else:
                messages.success(request, 'username or password is invalid', 'danger')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form':form})


def logout_user(request):
    logout(request)
    messages.success(request, 'logouted is successfuly', 'success')
    return redirect('home:main')


