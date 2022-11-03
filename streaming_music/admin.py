from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.



@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('genre',)
    search_fields = ['genre']
    list_filter = ['genre']


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('track', 'artist', 'uploaded_on','file')
    search_fields = ['track', 'artist', 'uploaded_on']
    list_filter = ['track', 'artist', 'uploaded_on']
    action = ['approve_song', 'delete']

    def approve_song(request, self, queryset):
        queryset.update(approved=True)




@admin.register(Album)
class AlbumAdmin(SummernoteModelAdmin):
    list_display = ('title', 'created_on', 'genre', 'image', 'description')
    search_fields = ['title', 'created_on', 'genre']
    list_filter = ['title', 'created_on', 'genre']
    action = ['delete']
    summernote_field = ('description',)




@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ['last_name', ]
    action = ['delete']

