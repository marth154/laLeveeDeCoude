from django.shortcuts import render
import requests

# Create your views here.
def random(request):
    response = requests.get('http://www.thecocktaildb.com/api/json/v1/1/random.php').json()
    print(response);
    return render(request, 'random.html', {'response': response})