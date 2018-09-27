# Sesión 7

### Para continuar...
1. Haga el siguiente flujo de trabajo utilizando git.
    
    ```git
    git fetch   # Para actualizar los tags que tiene el repositorio remoto
    git status  # revisa el estado de sus cambios
    git add .   # Agregue todos sus cambios
    git commit -m "<menaje>"
    ```
2. Tener cuidado con la configuración realizada en su proyecto local `settings.py`, respalde las credenciales de base de datos, antes de seguir al siguiente paso.
3. En este punto se han creado `tags` usando `git` para que accedan directamente a la versión requerida para avanzar con el proyecto, para esto ejecute el siguiente comando:
    
    ```git 
    git checkout tags/v.1.0.1
    git checkout -b v.1.0.1
    ```

4. En este paso verifique si se realizo las actualizaciones de directorios y ficheros del proyecto.

## Agregando librerías de terceros

### Agregando características en la aplicación `users`

1. Elegiremos el paquete de terceros `django-crispy-forms`, para agregarlo a los formularios. Para esto utilizar pipenv para instalar el paquete al proyecto.
    ```python
    pipenv install django-crispy-forms
    ```
2. Agregar al settings.py en la variable `INSTALLED_APPS`.
    ```python
        INSTALLED_APPS = [
            ...
            'crispy_forms',
            ...
        ]
    ```

3. Agregar y configurar la variable del paquete instalado previamente en el `settings.py`.
    ```python
    CRISPY_TEMPLATE_PACK = 'bootstrap4'
    ```

4. Editar el archivo html `templates/signup.html` especificamente cargue la librería en el template.
    ```
    {% extends 'base.html' %}
    {% load crispy_forms_tags %}
    ...
    ```

## Empezando con la aplicación `core`

Esta aplicación gestiona el ingreso, listado, modificación y eliminación de las películas. Además los usuarios del sistema podrán votar por su película favorita.

1. Agregar el primer modelo a la aplicación `core`, el modelo `Movie` con los siguientes campos (`title`, `plot`, `year`, `rating`, `website`).

    ```python
    NOT_RATED = 0
    RATED_G = 1
    RATED_PG = 2
    RATED_R = 3
    RATINGS = (
        (NOT_RATED, 'NR - Sin Clasificar'),
        (RATED_G, 'G - Audiencia General'),
        (RATED_PG, 'PG - Bajo supervision de los padres'),
        (RATED_R, 'R - Restringido'),
    )
    title = models.CharField(max_length=140) # Representa el título de la película
    plot = models.TextField()  # Permite agregar parrafos en este caso un argumento sobre la pelicula.
    year = models.PositiveIntegerField() # Indica el año de lanzamiento de la pelicula
    rating = models.IntegerField(choices=RATINGS, default=NOT_RATED) # Explicación
    website = models.URLField(blank=True)
    ```

2. Agregue el método `__str__` al modelo Movie, con formato `title` y `year`.

3. Ejecute las migraciones.
    
    ```python
    python manage.py makemigrations core
    python manage.py migrate core
    ```

4. Agregar al admin site de Django el modelo `Movie`. Agregar filtro por `rating`.

5. Crear vista para listar las peliculas - utilizando Vistas basadas en clase (VCBs), revisar la referencia: [link]( https://ccbv.co.uk/).

6. Usando vista basada en clase, `MovieList`.

    ```python
    from django.shortcuts import redirect
    from django.urls import reverse
    from django.views.generic import (ListView, DetailView, UpdateView, CreateView)

    class MovieList(ListView):
        model = Movie
    ```

7. Crear un fichero `urls.py` en la aplicación `core`, `core/urls.py`
8. Configurar el fichero `core/urls.py` para agregar la vista que se creo previamente.

    ```python
    from django.urls import path
    from . import views

    app_name = 'core'
    urlpatterns = [
        path('movies', views.MovieList.as_view(), name='MovieList'),
    ]
    ```

9. Enlazar la ruta principal del proyecto en `config/urls.py`
10. Crear un directorio para agrupar los HTMLs respectivos a las vistas de Movies, nombrar al directorio `templates/movies/` y crear `templates/movies/movie_detail.html`, `templates/movies/movie_list.html`
11. Agregar la vista de Detalle de Movies es decir `MoviesDetail`.
12. Configure la ruta en `core/urls.py`.

### Agregando paginación
1. Agregue en el modelo `Movie` que ordene por los campos `year`, `title`.
2. Modificar el html `templates/movies/movie_list.html` para agregar la paginación copiar el fragmento de html que se encuentra en el siguiente enlace [link](https://gist.github.com/betodev90/507a712e406f8f6e76604ab21cc295ec)
3. Utilizar el template tag de django para incluir fragmento de código.
    ```python
    {% include 'page.html' %}
    ```

4. Modificar la vista `MovieList`.
    ```python
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
    ```
5. A continuación avance con el capitulo de tests. En el directorio `core/tests` se encuentra el fichero para realizar las pruebas automaticas.
6. Se procede a crear un Test Automático de la vista MovieList y verificar su correcto funcionamiento. En el fichero `core/tests.py` agregar las siguientes importaciones.

    ```python
    # Libreria propia para hacer los Test
    from django.test import TestCase
    # Libreria de test para simular una solicitud request de una vista
    from django.test.client import RequestFactory
    # Libreria de django que obtiene el path / url metodo `reverse`
    from django.urls.base import reverse

    from .models import Movie
    from .views import MovieList
    ```

8. En el fichero `core/tests.py` crear la clase `class MovieListPaginationTestCase(TestCase)`
    
    ```python

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
    ```
9. Para ejecutar los tests.
    ```python
    python manage.py test
    ```

### Agregando modelo Persona

1. Crear un modelo `Person` en `core/models.py`.
    ```python
        class Person(models.Model):
            first_name = models.CharField(max_length=140)
            last_name = models.CharField(max_length=140)
            born = models.DateField()
            died = models.DateField(null=True, blank=True)
            objects = PersonManager()

            class Meta:
                ordering = ('last_name', 'first_name')

            def __str__(self):
                if self.died:
                    return '{}, {} ({}-{})'.format(
                        self.last_name,
                        self.first_name,
                        self.born,
                        self.died)
                return '{}, {} ({})'.format(
                        self.last_name,
                        self.first_name,
                        self.born)
    ```

2. En el modelo `Movie` defina que cada película tenga un director, pero cada director puede dirigir muchas películas para esto se establece un ForeignKey como puede ver a continuación:
    ```python
    # class Movie(models.Model):
    ...
    director = models.ForeignKey(
        to='Person',    # modelo a relacionar
        null=True,      # Puede ser null
        on_delete=models.SET_NULL, # Django necesita la instruccion de que hacer si el modelo referenciado es borrado, en este caso se mantiene NULL si el campo director es borrado.
        related_name='directed',    # Argumento opcional que indica el nombre que se utilizará para las consultas entre ambos modelos.
        blank=True)     # No requerido si se crea desde el admin.
    ...
    ```
3. En el modelo `Movie` agregar una columna `writers` que representa escritor con la definicion de que cada película puede ser escrita por varios escritores y un escritor puede escribir muchas peliculas.

    ```python
    ...
    writers = models.ManyToManyField(
        to='Person',
        related_name='writing_credits',
        blank=True
    )
    ...
    ```
4. En el modelo `Movie` agragar la columna `actors` con una relacion de muchos a muchos entre el modelo `Person` y `Movie` pero agregando un modelo intermedio que se debe crear llamado `Role`.

    ```python
    # class Movie(models.Model):
    ...
    actors = models.ManyToManyField(
        to='Person',
        through='Role',
        related_name='acting_credits',
        blank=True)
    ...
    ```

    ```python
        class Role(models.Model):
            movie = models.ForeignKey(Movie, on_delete=models.DO_NOTHING)
            person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
            name = models.CharField(max_length=140)

            def __str__(self):
                return "{} {} {}".format(self.movie_id, self.person_id, self.name)

            class Meta:
                unique_together = ('movie', 'person', 'name')
    ```

5. Crear las migraciones de la aplicación `core` con los comandos: `makemigrations` y `migrate`.


