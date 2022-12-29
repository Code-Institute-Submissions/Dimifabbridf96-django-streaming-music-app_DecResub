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
    list_display = ('title', 'first_name_artist','last_name_artist', 'uploaded_on', 'file')
    search_fields = ['song_title','first_name_artist','last_name_artist', 'uploaded_on']
    list_filter = ['title','first_name_artist','last_name_artist', 'uploaded_on']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'album', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email address', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """
        update the approved boolean in True if called
        """
        queryset.update(approved=True)