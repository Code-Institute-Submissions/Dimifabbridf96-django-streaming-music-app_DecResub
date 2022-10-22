from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse,request
from .models import Artist 


# Create your views here.
def hello(request):
    model = Artist
    return HttpResponse(model)



