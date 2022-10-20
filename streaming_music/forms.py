from .models import Audio_File
from django import forms


class AudioForm(forms.ModelForm):
    class Meta:
        model = 'audio_file'
        fields = [record ,]