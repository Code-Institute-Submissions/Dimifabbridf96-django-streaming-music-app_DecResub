from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import *
from .forms import *


# Create your views here.

class AlbumList(generic.ListView):
    model = Album
    paginate_by = 10
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
                #'album_form': AlbumForm()
            }
        )


def addAlbum(request):
    if request.method == 'POST':
        title = request.POST['title']
        #artist = request.POST['artist']
        image = request.FILES['image']
        description = request.POST['description']
        genre = request.POST['genre']

        form = Album(title=title, image=image, description=description, genre=genre)
        form.save()
        #Album.objects.create(title=title, artist=artist, genre=genre, image=image, description=description)
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

#
   # def post(self, request, title, *args, **kwargs):
   #     queryset = Album.objects.order_by('created_on')
   #     album = get_object_or_404(queryset, title=title)
   #     songs = Song.objects.all().filter(album=album)
   #     liked = False
   #     if album.likes.filter(id=self.request.user.id).exists():
   #         liked = True
   #         album_form = AlbumForm(data=request.POST)
#
   #         if album_form.is_valid():
   #             album = album_form.save(commit=False)
   #             album.album = album
   #             album.save()
   #         else:
   #             album_form = AlbumForm()
   #             
#
#
   #         return render(
   #            request,
   #            'albums_content.html',
   #            {
   #                'album': album,
   #                'songs': songs,
   #                'liked': liked,
   #                'album_form': AlbumForm()
   #            }
   #        )
#
#
#class Albumform(View):
#    def get(request, *args, **kwargs):
#        return render(
#            request, 
#            'add-album.html',
#            {
#                'album_form': AlbumForm()
#            }
#        )


def addArtist(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        #title = request.POST['title']
        ##artist = request.POST['artist']
        #image = request.POST['image']
        #description = request.POST['description']
        #genre = request.POST['genre']
#
        #form = Album(title=title, image=image, description=description, genre=genre)
        form1 = ArtistForm(request.POST, request.FILES)
        #Album.objects.create(title=title, artist=artist, genre=genre, image=image, description=description)
        form1.save()
        return redirect('/')
    
    return render(request, 'add-album.html',
    {
        'album_form': ArtistForm()
    }
    )


def removeSong(request, id, title):
    song = Song.objects.get(id=id)
    song.delete()
    return redirect('/')


def addSong(request):
    if request.method == 'POST':
        track = request.POST['title']
        artist_name = request.POST['artist_name']
        artist_surname = request.POST['artist_surname']
        file = request.FILES['file']

        form2 = Song(title=track, artist_name=artist_name, artist_surname=artist_surname, file=file)
        form2.save()
        #Album.objects.create(title=title, artist=artist, genre=genre, image=image, description=description)
        return redirect('/')
    return render(request, 'add-song.html',
    {
        'song_form': SongForm()
    }
    )