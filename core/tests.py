from django.test import TestCase

from django.test.client import RequestFactory
from django.urls.base import reverse

from .models import Movie
from .views import MovieList


class MovieListPaginationTestCase(TestCase):
    ACTIVE_PAGINATION_HTML = """
    <li class="page-item active">
      <a href="{}?page={}" class="page-link">{}</a>
    </li>
    """

    def setUp(self):
        for n in range(15):
            Movie.objects.create(title='Title {}'.format(n),
                year=1990 + n
            )

    def testFirstPage(self):
        # Obtiene el path desde el name de una url previamente definida
        movie_list_path = reverse('core:MovieList') # /movies
        # Hace la solicitud objeto request a una vista falsa
        request = RequestFactory().get(path=movie_list_path)
        # Llamado a la vista obtiene un objeto HttResponse / response
        response = MovieList.as_view()(request)

        # Metodos de la libreria Test de django que verifica que se debe obtener lo esperado
        self.assertEqual(200, response.status_code)
        self.assertTrue(response.context_data['page_is_first'])
        self.assertFalse(response.context_data['page_is_last'])
        self.assertInHTML(
            self.ACTIVE_PAGINATION_HTML.format(movie_list_path, 1, 1),
            response.rendered_content
        )