from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Album, Song


class TestSong(TestCase):

    def test_song_title_unique(self):
        album = Song.objects.create('title':'Youngblood')
        album1 = Song.objects.create('title':'Youngblood')
        existing_items = Song.objects.filter(title='Youngblood')
        self.assertEqual(len(existing_items), 0)

    def test_first_and_last_name_artist_string_method_returns_data(self):
        item = Item.objects.create('first_name_artist':'Dimi', 'last_name_artist':'Fabbri')
        self.assertEqual(str(item), 'Dimi', 'Fabbri')
    
    def test_approved_default_to_false():
        song = Song.objects.create('title':'Youngblood', 'first_name_artist':'Dimi', 'last_name_artist':'Fabbri', 'file': 'audio', 'album':'Youngblood')
        self.assertFalse(song.approved)