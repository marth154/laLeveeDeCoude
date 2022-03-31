from django.http import HttpResponseRedirect
from django.contrib.auth import logout


# Create your views here.
    
    
def lldc_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
        