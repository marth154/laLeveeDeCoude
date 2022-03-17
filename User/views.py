from django.shortcuts import render

# from .models import User
from django.contrib.auth.models import User
from .forms import RegisterForms, LoginForms
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
# Create your views here.


def loginCredentials(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get(
            "username"), password=request.POST.get("password"))
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            form = LoginForms()
            context = {
                'form': form,
                'notExisting': "true"
            }
            return render(request, 'login.html', context)
    if request.method == 'GET':
        form = LoginForms()
        context = {
            'form': form
        }
        return render(request, 'login.html', context)


def registerCredentials(request):
    if request.method == 'POST':
        user = User.objects.filter(email__exact=request.POST.get("email"))
        if(user):
            form = RegisterForms()
            context = {
                'form': form,
                'existing': "true"
            }
            return render(request, 'register.html', context)
        else:
            user = User.objects.create_user(
                username=request.POST.get("username"), email=request.POST.get("email"), password=request.POST.get("password"))
            user.save()
            login(request, user)
            return HttpResponseRedirect('/')
    if request.method == 'GET':
        form = RegisterForms()
        context = {
            'form': form
        }
        return render(request, 'register.html', context)


def bar(request):
    return render(request, 'bar.html')
