from django.shortcuts import render

# from .models import User  
from django.contrib.auth.models import User
from .forms import RegisterForms
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def login(request):
    return render(request, 'login.html')

def bar(request):
    return render(request, 'bar.html')

def register(request):
    if request.method == 'POST':
        user = User.objects.create_user(
            username=request.POST.get("username"), email=request.POST.get("email"), password=request.POST.get("password"))
        print(user)
        user.save()
        return HttpResponse("Do something")
    else:
        form = RegisterForms()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)
