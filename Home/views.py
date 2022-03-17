from django.shortcuts import render

# Create your views here.


def home(request):
    if request.user:
        return render(request, 'home.html')
    else:
        print("User isn't authenticated")
        return render(request, 'home.html')
