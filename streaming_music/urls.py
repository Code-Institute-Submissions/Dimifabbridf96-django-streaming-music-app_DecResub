from . import views
from django.urls import path

urlpatterns = [
    path('audio', views.Audio_File.as_view(), name='audio')
]