from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .forms import SongForm, AlbumForm
from .models import Song, Album


class TestSongForm(TestCase):

    def test_song_form_is_valid(self):
        image = SimpleUploadedFile(name="file.jpg", content=b'', content_type="image/jpeg")
        album = Album.objects.create(title='Youngblood', image=image, description='description', genre='Pop')
        audio = SimpleUploadedFile(name="file.mp3", content=b'', content_type="audio/mpeg")
        form = SongForm({
            'title': 'Youngblood',
            'first_name_artist': 'Dimi',
            'last_name_artist':'Fabbri',
            'file': audio,
            'album': album

        })
        self.assertTrue(form.is_valid())

    def test_title_in_song_is_required(self):
        form = SongForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_first_name_artist_in_song_is_required(self):
        form = SongForm({'first_name_artist': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('first_name_artist', form.errors.keys())
        self.assertEqual(form.errors['first_name_artist'][0], 'This field is required.')

    def test_last_name_artist_in_song_is_required(self):
        form = SongForm({'last_name_artist': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('last_name_artist', form.errors.keys())
        self.assertEqual(form.errors['last_name_artist'][0], 'This field is required.')

    def test_album_in_song_is_required(self):
        form = SongForm({'album': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('album', form.errors.keys())
        self.assertEqual(form.errors['album'][0], 'This field is required.')


class TestAlbumForm(TestCase):

    def test_album_form_is_valid(self):
        image = SimpleUploadedFile(name="file.jpg", content=b'', content_type="image/jpeg")
        form = AlbumForm({
            'title': 'Youngblood',
            'image': image,
            'description': 'Fabbri',
            'genre': 'Pop'

        })
        self.assertTrue(form.is_valid())

    def test_title_in_album_is_required(self):
        form = AlbumForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_genre_in_album_is_required(self):
        form = AlbumForm({'genre': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('genre', form.errors.keys())
        self.assertEqual(form.errors['genre'][0], 'This field is required.')
