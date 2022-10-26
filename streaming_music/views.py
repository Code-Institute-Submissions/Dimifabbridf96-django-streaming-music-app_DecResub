from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from .models import *


# Create your views here.

class AlbumList(generic.ListView):
    model = Album
    paginate_by = 10
    queryset = Album.objects.order_by('created_on')
    template_name = 'albums.html'


