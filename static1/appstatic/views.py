from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect

# Create your views here.
def home(request):
    return HttpResponseRedirect("/static/index.html")

