from django.contrib import admin
from .models import *
# Register your models here.



@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('genre',)
    search_fields = ['genre']
    list_filter = ['genre']


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('song_title','song_artist','uploaded_on', 'song_file')
    search_fields = ['song_title','song_artist','uploaded_on']
    list_filter = ['song_title','song_artist','uploaded_on']
    action = ['approve_song']

    def approve_song(request, self, queryset):
        queryset.update(approved=True)




@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('album_artist', 'album_title', 'created_on', 'album_genre', 'songs', 'album_image')
    search_fields = ['album_artist', 'album_title', 'created_on', 'album_genre']
    list_filter = ['album_artist', 'album_title', 'created_on', 'album_genre']




@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('artist_name', 'artist_surname')
    search_fields = ['artist_surname',]


