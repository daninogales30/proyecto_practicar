from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from movies.models import *


# Create your views here.
@login_required
def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', context={'movies': movies})

@login_required
def movies_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/movies_detail.html', context={'movie': movie})

@login_required
def lista_actores(request):
    actores = Actor.objects.all()
    return render(request, 'movies/lista_actores.html', context={'actores': actores})

@login_required
def actor_detail(request, actor_id):
    actor = get_object_or_404(Actor, pk=actor_id)
    return render(request, 'movies/actor_detail.html', context={'actor': actor})

@login_required
def lista_directores(request):
    directores = Director.objects.all()
    return render(request, 'movies/lista_directores.html', context={'directores': directores})

@login_required
def director_detail(request, director_id):
    director = get_object_or_404(Director, pk=director_id)
    return render(request, 'movies/director_detail.html', context={'director': director})

@login_required
def pelis_2022(request):
    peliculas = Movie.objects.filter(release_date__year='2022')
    return render(request, 'movies/pelis_2022.html', context={'peliculas': peliculas})

@login_required
def pelis_rating(request):
    peliculas = Movie.objects.filter(rating__gt=8)
    return render(request, 'movies/pelis_rating.html', context={'peliculas': peliculas})
