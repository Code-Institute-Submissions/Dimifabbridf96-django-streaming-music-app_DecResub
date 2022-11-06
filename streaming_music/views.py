from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import *
from .forms import AlbumForm


# Create your views here.

class AlbumList(generic.ListView):
    model = Album
    model = Genre
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
        title = request.POST.get('title')
        artist = request.POST.get('artist')
        image = request.POST.get('image')
        genre = request.POST.get('genre')
        description = request.POST.get('description')
        Album.objects.create(title=title, artist=artist, genre=genre, image=image, description=description)

        return redirect('AlbumList')
    return render(request, 'add-album.html',
    {
        'album_form': AlbumForm()
    }
    )


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