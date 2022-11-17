from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import *
from .forms import *


# Create your views here.

class AlbumList(generic.ListView):
    model = Album
    paginate_by = 6
    queryset = Album.objects.order_by('created_on')
    template_name = 'albums.html'


class AlbumView(View):
    def get(self, request, title, *args, **kwargs):
        queryset = Album.objects.order_by('created_on')
        album = get_object_or_404(queryset, title=title)
        songs = Song.objects.all().filter(album=album)
        liked = False
        if album.likes.filter(id=self.request.user.id).exists():
            liked = True
        return render(
            request,
            'albums_content.html',
            {
                'album': album,
                'songs': songs,
                'liked': liked,
            }
        )


def addAlbum(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            image = request.FILES['image']
            if image.content_type == 'audio/mpeg':
                messages.error(request, 'Image not added, file needs to a jpg file, please try again')
            description = form.cleaned_data['description']
            genre = form.cleaned_data['genre']
            form.save()
        return redirect('/')
    return render(request, 'add-album.html',
    {
        'album_form': AlbumForm()
    }
    )


def deleteAlbum(request, id, title):
    album = Album.objects.get(id=id)
    album.delete()
    return redirect('/')

##def addArtist(request):
##    if request.method == 'POST':
##        first_name = form2.cleaned_data['first_name']
##        last_name = form2.cleaned_data['last_name']
##        form1 = ArtistForm(request.POST, request.FILES)
##        form1.save()
##        return redirect('/')
 #   
 #   return render(request, 'add-album.html',
 #   {
 #       'album_form': ArtistForm()
 #   }
 #   )


def removeSong(request, id, title):
    song = Song.objects.get(id=id)
    song.delete()
    return redirect('/')


def addSong(request):
    if request.method == 'POST':
        form2 = SongForm(request.POST, request.FILES)
        if form2.is_valid():
            title = form2.cleaned_data['title']
            first_name_artist = form2.cleaned_data['first_name_artist']
            last_name_artist = form2.cleaned_data['last_name_artist']
            album = form2.cleaned_data['album']
            file = request.FILES['file']
            if file.content_type != 'audio/mpeg':
                messages.error(request, 'Song not added, file needs to be mp3, please try again')
            else:
                form2.save()
                messages.success(request, 'Song added succesfully')
        return redirect('/')
    return render(request, 'add-song.html',
    {
        'song_form': SongForm()
    })