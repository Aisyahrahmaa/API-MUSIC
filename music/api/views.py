from django.shortcuts import render
from .models import Album,Song,Review
from rest_framework import viewsets
from .serializers import AlbumSerializer, SongSerializer, ReviewSerializer

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')


class AlbumViewSet(viewsets.ModelViewSet):
	queryset =  Album.objects.all()
	serializer_class = AlbumSerializer
 
class SongViewSet(viewsets.ModelViewSet):
	queryset = Song.objects.all()
	serializer_class = SongSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

