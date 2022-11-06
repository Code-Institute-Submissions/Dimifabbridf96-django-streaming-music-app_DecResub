from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.AlbumList.as_view(), name='home'),
    #path('add/', views.Albumform.as_view(), name='add'),
    path('<slug:title>/', views.AlbumView.as_view(), name='albums'),
    ]