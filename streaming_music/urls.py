from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.AlbumList.as_view(), name='audio'),
    path('summernote/', include('django_summernote.urls')),
]