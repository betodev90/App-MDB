from django.shortcuts import render
from django.views.generic import (ListView, DetailView, UpdateView, CreateView)

from .models import Movie

class MovieList(ListView):
    model = Movie
    template_name = 'movies/movie_list.html'


class MovieDetail(DetailView):
    model = Movie