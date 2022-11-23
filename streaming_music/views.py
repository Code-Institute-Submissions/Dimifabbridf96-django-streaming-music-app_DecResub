from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from PIL import Image
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
        album = get_object_or_404(Album, title=title)
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

    def post(self, request, title, *args, **kwargs):
        album = get_object_or_404(Album, title=title)
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


class AlbumLike(View):
    def post(self, request, title):
        album = get_object_or_404(Album, title=title)
        if album.likes.filter(id=request.user.id).exists():
            album.likes.remove(request.user)
        else:
            album.likes.add(request.user)
        return HttpResponseRedirect(reverse('albums', args=[title]))


def addAlbum(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            genre = form.cleaned_data['genre']
            image = form.cleaned_data['image']
            form.save()
            messages.success(request, 'Image added succesfully')
        return redirect('/')
    return render(request, 'add-album.html',
    {
        'album_form': AlbumForm()
    }
    )


def editAlbum(request, album_id):

    album = get_object_or_404(Album, id=album_id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
        return redirect('/')
    form = AlbumForm(instance=album)
    context = {
        'form': form
    }

    return render(request, 'edit-album.html', context)


def deleteAlbum(request, id, title):
    album = Album.objects.get(id=id)
    album.delete()
    return redirect('/')


def addSong(request):
    if request.method == 'POST':
        form2 = SongForm(request.POST, request.FILES)
        if form2.is_valid():
            title = form2.cleaned_data['title']
            first_name_artist = form2.cleaned_data['first_name_artist']
            last_name_artist = form2.cleaned_data['last_name_artist']
            album = form2.cleaned_data['album']
            file = request.FILES.get('file')
            print(file)
            if file is None or file.content_type == 'audio/mpeg':
                form2.save()
                messages.success(request, 'Song added succesfully')
            else:
                messages.error(request, 'Song not added, file needs to be mp3, please try again')
        return redirect('/')
    return render(request, 'add-song.html',
    {
        'song_form': SongForm()
    })


def editSong(request, song_id):

    song = get_object_or_404(Song, id=song_id)
    if request.method == 'POST':
        form = SongForm(request.POST, instance=song)
        if form.is_valid():
            form.save()
        return redirect('/')
    form = SongForm(instance=song)
    context = {
        'form': form
    }

    return render(request, 'edit-song.html', context)


def removeSong(request, id, title):
    song = Song.objects.get(id=id)
    song.delete()
    return redirect('/')
