from django.db import models
from django.urls import reverse
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=30)

    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_genres', blank=True)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=30)
    code = models.IntegerField()
    role = models.CharField(max_length=20)
    filmography = models.TextField()

    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_directors', blank=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    code = models.IntegerField()
    title_ko = models.CharField(max_length=50)
    title_en = models.CharField(max_length=50)
    audience = models.IntegerField()
    opening_year = models.IntegerField()
    runtime = models.IntegerField()

    genres = models.ManyToManyField(Genre, related_name="movies", blank=True)
    directors = models.ManyToManyField(Director, related_name="movies", blank=True)

    naver_detail_url = models.TextField()
    naver_thumbnail_url = models.TextField()    
    naver_score = models.FloatField()

    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies', blank=True)

    def __str__(self):
        return self.title_ko


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField()
    score = models.FloatField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)