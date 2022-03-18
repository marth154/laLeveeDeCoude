from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="/login")
def home(request):
    if request.user:
        return render(request, 'home.html')
    else:
        print("User isn't authenticated")
        return render(request, 'home.html')
