from django import forms
from .models import Album, Song, Artist


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('title', 'image', 'description', 'genre')


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ('first_name', 'last_name', 'image')


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ('title', 'artist', 'file', 'album')