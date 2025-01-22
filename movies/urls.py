from django.urls import path

from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_id>/detail', views.movies_detail, name='movies_detail'),
    path('actores/', views.lista_actores, name='lista_actores'),
    path('actor/<int:actor_id>/detail', views.actor_detail, name='actor_detail'),
    path('directors', views.lista_directores, name='lista_directores'),
    path('directors/<int:director_id>/detail', views.director_detail, name='director_detail'),
    path('2022/', views.pelis_2022, name='pelis_2022'),
    path('rating/', views.pelis_rating, name='pelis_rating')
]