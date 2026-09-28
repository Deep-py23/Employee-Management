from django.shortcuts import render, redirect
from . forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth


def register(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else :
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form':form})



def login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method=='POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('home')

    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})


def logout(request):
    auth.logout(request)
    return redirect('home')
