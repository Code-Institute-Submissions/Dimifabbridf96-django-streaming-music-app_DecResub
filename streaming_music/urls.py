from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.AlbumList.as_view(), name='home'),
    path('<slug:title>/', views.AlbumView.as_view(), name='albums')    
    ]