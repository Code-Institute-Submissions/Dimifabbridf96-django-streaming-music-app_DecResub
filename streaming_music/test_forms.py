from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .forms import SongForm
from .models import Song, Album


class TestForm(TestCase):

    def test_song_(self):
        image = SimpleUploadedFile(name="file.jpg", content=b'', content_type="image/jpeg")
        album = Album.objects.create(title='Youngblood' , image=image , description='description', genre='Pop')
        audio = SimpleUploadedFile(name="file.mp3", content=b'', content_type="audio/mpeg")
        form = SongForm({
            'title': 'Youngblood',
            'first_name_artist': 'Dimi',
            'last_name_artist':'Fabbri',
            'file': audio,
            'album': album

        })

        self.assertTrue(form.is_valid())

