from django import forms
from .models import *


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('title', 'image', 'description', 'genre')


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ('title', 'first_name_artist','last_name_artist', 'file', 'album')