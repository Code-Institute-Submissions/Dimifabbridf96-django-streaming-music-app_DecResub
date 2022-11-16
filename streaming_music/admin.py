from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.



@admin.register(Album)
class AlbumAdmin(SummernoteModelAdmin):
    list_display = ('title', 'created_on', 'genre', 'image', 'description')
    search_fields = ['title', 'created_on', 'genre']
    list_filter = ['title', 'created_on', 'genre']
    action = ['delete']
    summernote_field = ('description',)


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title','uploaded_on', 'file', 'artist_name', 'artist_surname')
    search_fields = ['song_title','artist_name','artist_surname' ,'uploaded_on']
    list_filter = ['title','artist_name', 'artist_surname','uploaded_on']
    action = ['approve_song']

    def approve_song(request, self, queryset):
        queryset.update(approved=True)

