from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from PIL import Image
from .models import *
from .forms import *


# Create your views here.

class AlbumList(generic.ListView):
    model = Album
    paginate_by = 6
    queryset = Album.objects.order_by('-created_on')
    template_name = 'albums.html'


class AlbumView(View):
    def get(self, request, id, *args, **kwargs):
        """
        get the content of the album request 
        """
        queryset = Album.objects.order_by('created_on')
        album = get_object_or_404(Album, id=id)
        songs = Song.objects.all().filter(album=album)
        comments = album.comments.filter(approved=True).order_by('-created_on')
        liked = False
        if album.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'albums_content.html',
            {
                'album': album,
                'songs': songs,
                'comments': comments,
                'commented': False,
                'liked': liked,
                'comment_form': CommentForm()
            },
        )

    def post(self, request, id, *args, **kwargs):
        """
        post the likes and comment of the album request
        """
        album = get_object_or_404(Album, id=id)
        songs = Song.objects.all().filter(album=album)
        comments = album.comments.filter(approved=True).order_by('-created_on')
        liked = False
        if album.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.album = album
            comment.save()
        else: 
            comment_form = CommentForm()

        return render(
            request,
            'albums_content.html',
            {
                'album': album,
                'songs': songs,
                'comments': comments,
                'commented': True,
                'liked': liked,
                'comment_form': CommentForm()
            },
        )


class AlbumLike(View):
    def post(self, request, id):
        """
        post the likes from request.user
        """
        album = get_object_or_404(Album, id=id)
        if album.likes.filter(id=request.user.id).exists():
            album.likes.remove(request.user)
        else:
            album.likes.add(request.user)
        return HttpResponseRedirect(reverse('albums', args=[id]))


@login_required(login_url="/accounts/login/")
def addAlbum(request):
    """
        add the album create from the user
        """
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            genre = form.cleaned_data['genre']
            image = form.cleaned_data['image']
            album = form.save(commit=False)
            album.owner = request.user
            album.save()
            messages.success(request, 'Image added succesfully')
            print(album.owner)
        return redirect('/')
    return render(request, 'add-album.html',
    {
        'album_form': AlbumForm()
    }
    )


@login_required(login_url="/accounts/login/")
def editAlbum(request, album_id):
    """
        edit the album requested 
        """

    album = get_object_or_404(Album, id=album_id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            messages.success(request, 'Album edited succesfully')

        return redirect('/')
    form = AlbumForm(instance=album)
    context = {
        'form': form
    }

    return render(request, 'edit-album.html', context)


@login_required(login_url="/accounts/login/")
def deleteAlbum(request, album_id, id):
    """
        edit the album requested 
        """
    album = Album.objects.get(id=album_id)
    album.delete()
    messages.success(request, 'Album deleted succesfully')
    return redirect('/')


@login_required(login_url="/accounts/login/")
def addSong(request):
    """
    add the song create from the user
    """
    
    if request.method == 'POST':
        form2 = SongForm(request.POST, request.FILES)
        if form2.is_valid():
            title = form2.cleaned_data['title']
            first_name_artist = form2.cleaned_data['first_name_artist']
            last_name_artist = form2.cleaned_data['last_name_artist']
            file = request.FILES.get('file')
            album = form2.cleaned_data['album']
            if request.user == album.owner or request.user.is_superuser:
                messages.success(request, 'Request allowed')
            else:
                messages.error(request, "If you are not the owner of the album you can't add song in it, please select your own album")
                return redirect('/add1')
            if file is None:
                messages.error(request, 'Song not added, please upload an mp3 file')
            elif file.content_type == 'audio/mpeg': 
                messages.success(request, 'Song added succesfully')
                form2.save()
            else:
                messages.error(request, 'Song not added, file needs to be an mp3 file')
        return redirect('/')
    return render(request, 'add-song.html',
    {
        'song_form': SongForm()
    })


@login_required(login_url="/accounts/login/")
def editSong(request, song_id):
    """
        edit the song requested 
    """
    song = get_object_or_404(Song, id=song_id)
    if request.method == 'POST':
        form = SongForm(request.POST, instance=song)
        if form.is_valid():
            form.save()
            messages.success(request, 'Song edited succesfully')

        return redirect('/')
    form = SongForm(instance=song)
    context = {
        'form': form
    }

    return render(request, 'edit-song.html', context)


@login_required(login_url="/accounts/login/")
def removeSong(request, song_id, id):
    """
        remove the song requested 
    """
    song = Song.objects.get(id=song_id)
    song.delete()
    messages.success(request, 'Song deleted succesfully')
    return redirect('/')
