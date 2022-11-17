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

   # def clean_file(self, *args, **kwargs):
   #     file = self.cleaned_data.get('file')
   #     if file.content_type != 'audio/mpeg':
   #         raise forms.ValidationError('Your file needs to be an mp3 ')
   #     return file