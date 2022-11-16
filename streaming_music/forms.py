from django import forms
from .models import *


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('title', 'image', 'description', 'genre')


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ('title', 'artist_name','artist_surname', 'file','album')