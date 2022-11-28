from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.AlbumList.as_view(), name='home'),
    path('<int:id>/', views.AlbumView.as_view(), name='albums'),
    path('like/<int:id>', views.AlbumLike.as_view(), name='albums_like'),
    ]