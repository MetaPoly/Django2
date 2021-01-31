from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {"info": "my name is sean, I like python"})