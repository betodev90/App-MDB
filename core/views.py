from django.shortcuts import render
from django.views.generic import (ListView, DetailView, UpdateView, CreateView)

from .models import Movie

class MovieList(ListView):
    model = Movie
    paginate_by = 10
    template_name = 'movies/movie_list.html'

    def get_context_data(self, **kwargs):
        ctx = super(MovieList, self).get_context_data(**kwargs)
        page = ctx['page_obj']
        paginator = ctx['paginator']
        ctx['page_is_first'] = (page.number == 1)
        ctx['page_is_last'] = (page.number == paginator.num_pages)
        return ctx

class MovieDetail(DetailView):
    model = Movie