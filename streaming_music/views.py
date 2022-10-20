from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Audio_File
from .forms import AudioForm
# Create your views here.


def Audio_File(request):
    if request.method == 'POST':
        form = AudioForm(request.POST, request.files)
    if form.is_valid():
        form.save()
        return HttpResponse('succesfully uploaded')
    else:
        form = AudioForm()
    return render(request, 'audio_form.html', {'form': form})



