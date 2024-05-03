from django.db import models
from django.contrib.auth.models import User


class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

def __str__(self):
    return self.album_title + ' - ' + self.artist

class Song(models.Model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    file_type =models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)

def __str__(self):
    return self.song_title

class Review(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.song.song_title} -{self.rating}"
