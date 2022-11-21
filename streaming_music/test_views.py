from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Album, Song


class TestViews(TestCase):

    def test_get_album_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'albums.html')

    def test_get_add_album_page(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add-album.html')
        
    def test_get_edit_album_page(self):
        image = SimpleUploadedFile(name="file.jpg", content=b'', content_type="image/jpeg")
        album = Album.objects.create(title='Youngblood' , image= image , description='description', genre='Pop')
        response = self.client.get(f'/edit/{album.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit-album.html') 

    def test_can_add_an_album(self):
        image = SimpleUploadedFile(name="file.jpg", content=b'', content_type="image/jpeg")
        response = self.client.post('/add',{'title':'Youngblood' , 'image': image , 'description':'description', 'genre':'Pop'} )
        self.assertRedirects(response, '/')

    def test_can_delete_album(self):
        image = SimpleUploadedFile(name="file.jpg", content=b'', content_type="image/jpeg")
        album = Album.objects.create(title='Youngblood' , image= image , description='description', genre='Pop')
        response = self.client.get(f'/{album.id}/remove/{album.id}')
        self.assertRedirects(response, '/')
        existing_items = Album.objects.filter(id=album.id)
        self.assertEqual(len(existing_items), 0)

    def test_can_edit_album(self):
        image = SimpleUploadedFile(name="file.jpg", content=b'', content_type="image/jpeg")
        album = Album.objects.create(title='Youngblood' , image=image , description='description', genre='Pop')
        response = self.client.post(f'/edit/{album.id}', {'title':'Youngblood' , 'image': image, 'description':'Amazing Album', 'genre':'Pop'})
        self.assertRedirects(response, '/')
        updated_item = Album.objects.get(id=album.id)
        self.assertEqual(updated_item.description, 'Amazing Album')

    def test_get_song_list(self):
        image = SimpleUploadedFile(name="file.jpg", content=b'', content_type="image/jpeg")
        album = Album.objects.create(title='Youngblood', image=image , description='description', genre='Pop')
        response = self.client.get(f'/{album.title}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'albums_content.html')

    def test_get_add_song_page(self):
        response = self.client.get('/add1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add-song.html')
    
    def test_can_add_a_song(self):
        audio = SimpleUploadedFile(name="file.mp3", content=b'', content_type="audio/mpeg")
        response = self.client.post('/add1',{'title':'Youngblood', 'first_name_artist':'Dimi','last_name_artist':'Fabbri', 'file': audio, 'album':'Youngblood'} )
        self.assertRedirects(response, '/')

    def test_can_delete_song(self):
        image = SimpleUploadedFile(name="file.jpg", content=b'', content_type="image/jpeg")
        album = Album.objects.create(title='Youngblood' , image=image , description='description', genre='Pop')
        song = Song.objects.create(title='Youngblood', first_name_artist='Dimi', last_name_artist='Fabbri', file= 'audio', album=album)
        response = self.client.get(f'/{album.title}/delete/{song.id}')
        self.assertRedirects(response, '/')
        existing_items = Song.objects.filter(id=song.id)
        self.assertEqual(len(existing_items), 0)
    
    #def test_can_edit_song(self):
    #    audio = SimpleUploadedFile(name="file.mp3", content=b'', content_type="audio/mpeg")
    #    image = SimpleUploadedFile(name="file.jpg", content=b'', content_type="image/jpeg")
    #    album = Album.objects.create(title='Youngblood' , image=image , description='description', genre='Pop')
    #    song = Song.objects.create(title='Youngblood', first_name_artist='Dimi', last_name_artist='Fabbri', file= audio, album=album)
    #    response = self.client.post(f'/edit1/{song.id}', {'title':'Young', 'first_name_artist':'Dimi', 'last_name_artist':'Fabbri', 'file':'audio', 'album':album})
    #    self.assertRedirects(response, '/')
    #    updated_item = Song.objects.get(id=song.id)
    #    self.assertEqual(updated_item.title, 'Young')
        
    def test_get_edit_song_page(self):
        image = SimpleUploadedFile(name="file.jpg", content=b'', content_type="image/jpeg")
        album = Album.objects.create(title='Youngblood' , image=image , description='description', genre='Pop')
        song = Song.objects.create(title='Youngblood', first_name_artist='Dimi', last_name_artist='Fabbri', file= 'audio', album=album)
        response = self.client.get(f'/edit1/{song.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit-song.html')
        
    