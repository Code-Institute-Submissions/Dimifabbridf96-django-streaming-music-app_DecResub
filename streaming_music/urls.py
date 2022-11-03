from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.AlbumList.as_view(), name='home'),
    path('<slug:title>/', views.SongList.as_view(), name='songs'),
    ]