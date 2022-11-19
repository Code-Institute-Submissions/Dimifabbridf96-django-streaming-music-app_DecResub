from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Album, Song


class TestViews(TestCase):

    def test_get_album_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'albums.html')

    def test_get_add_album_page(self):
        response = self.client.get('add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add-album.html')
        
    def test_get_edit_album_page(self):
        album = Album.objects.create('title':'Youngblood', 'first_name_artist':'Dimi', 'last_name_artist':'Fabbri', 'file': 'audio', 'album':'Youngblood')
        response = self.client.get(f'/edit/{album.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_album.html') 

    def test_can_add_an_album(self):
        image = SimpleUploadedFile("file.jpg", "file_content", content_type="image/jpeg")
        response = self.client.post('add/',{'title':'Youngblood' , 'image': 'image' , 'description':'description', 'genre':'Pop'} )
        self.assertRedirects(response, '/')

    def test_can_delete_album(self):
        album = Album.objects.create('title':'Youngblood' , 'image': 'image' , 'description':'description', 'genre':'Pop')
        response = self.client.get(f'<slug:title>/remove/{album.id}')
        self.assertRedirects(response, '/')
        existing_items = Album.objects.filter(id=album.id)
        self.assertEqual(len(existing_items), 0)

    def test_can_edit_album(self):
        album = Album.objects.create('title':'Youngblood' , 'image': 'image' , 'description':'description', 'genre':'Pop')
        response = self.client.post(f'/edit/{song.id}', {'title':'Youngblood' , 'image': 'image' , 'description':'Amazing Album', 'genre':'Pop'})
        self.assertRedirects(response, '/')
        updated_item = Album.objects.get(id=album.id)
        self.assertEqual(updated_item.description, 'Amazing Album')

    def test_get_song_list(self):
        response = self.client.get('<slug:title>/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'albums_content.html')

    def test_get_add_song_page(self):
        response = self.client.get('add1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add-song.html')
    
    def test_can_add_a_song(self):
        audio = SimpleUploadedFile("file.mp3", "file_content", content_type="audio/mpeg")
        response = self.client.post('add1/',{'title':'Youngblood', 'first_name_artist':'Dimi','last_name_artist':'Fabbri', 'file': 'audio', 'album':'Youngblood'} )
        self.assertRedirects(response, '/')

    def test_can_delete_song(self):
        song = Song.objects.create('title':'Youngblood', 'first_name_artist':'Dimi', 'last_name_artist':'Fabbri', 'file': 'audio', 'album':'Youngblood')
        response = self.client.get(f'<slug:title>/delete/{song.id}')
        self.assertRedirects(response, '/')
        existing_items = Song.objects.filter(id=song.id)
        self.assertEqual(len(existing_items), 0)
    
    def test_can_edit_song(self):
        song = Song.objects.create('title':'Youngblood', 'first_name_artist':'Dimi', 'last_name_artist':'Fabbri', 'file': 'audio', 'album':'Youngblood')
        response = self.client.post(f'/edit/{song.id}', {'title':'Youngblood', 'first_name_artist':'Alessio', 'last_name_artist':'Fabbri', 'file': 'audio', 'album':'Youngblood'})
        self.assertRedirects(response, '/')
        updated_item = Song.objects.get(id=item.id)
        self.assertEqual(updated_item.first_name_artist, 'Alessio')
        
    def test_get_edit_song_page(self):
        song = Song.objects.create('title':'Youngblood', 'first_name_artist':'Dimi', 'last_name_artist':'Fabbri', 'file': 'audio', 'album':'Youngblood')
        response = self.client.get(f'/edit/{song.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_song.html')
        
    