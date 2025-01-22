from django.db import models

class Director(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(null=False, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
    release_date = models.DateField()
    rating = models.IntegerField()
    summary = models.TextField(max_length=1000)

    def __str__(self):
        return self.title

class Actor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    movies = models.ManyToManyField(Movie)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
