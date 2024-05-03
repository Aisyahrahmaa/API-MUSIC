from .models import Album,Song, Review
from rest_framework import serializers

class AlbumSerializer(serializers.ModelSerializer):
		class Meta:
			model = Album
			fields = '__all__' #menampilkan semua field pada class Album

class SongSerializer(serializers.ModelSerializer):
		class Meta:
			model = Song
			fields = ('album', 'song_title')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'