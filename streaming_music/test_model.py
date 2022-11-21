from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Album, Song


class TestSong(TestCase):

    def test_song_title_string_method_return_title(self):
        album = Album.objects.create(title='Youngblood', image='image' , description='description', genre='Pop')
        song = Song.objects.create(title='Youngblood', first_name_artist='Dimi', last_name_artist='Fabbri', file= 'audio', album=album)
        self.assertEqual(str(song.title), 'Youngblood')
