from .models import Album,Song
from rest_framework import serializers

class AlbumSerializer(serializers.ModelSerializer):
		class Meta:
			model = Album
			fields = '__all__' #menampilkan semua field pada class Album

class SongSerializer(serializers.ModelSerializer):
		class Meta:
			model = Song
			fields = ('album', 'song_title')