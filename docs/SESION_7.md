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

5. Crear vista para listar las peliculas - utilizando Vistas basadas en clase (VCBs), revisar la referencia: [link]( https://ccbv.co.uk/){:target="_blank"}.

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
2. Modificar el html `templates/movies/movie_list.html` para agregar la paginación copiar el fragmento de html que se encuentra en el siguiente enlace [link](https://gist.github.com/betodev90/507a712e406f8f6e76604ab21cc295ec){:target="_blank"}
3. Utilizar el template tag de django para incluir fragmento de código.
    ```python
    {% include 'page.html' %}
    ```