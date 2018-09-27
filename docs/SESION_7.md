# Sesión 7

### Para continuar...
1. Haga el siguiente flujo de trabajo utilizando git.
    
    ```git
    git status  # revisa el estado de sus cambios
    git add .   # Agregue todos sus cambios
    git commit -m "<menaje>"
    ```

2. En este punto se han creado `tags` usando `git` para que accedan directamente a la versión requerida para avanzar con el proyecto, para esto ejecute el siguiente comando:
    
    ```git 
    git checkout tags/v.1.0.1
    ```

3. En este paso verifique si se realizo las actualizaciones de directorios y ficheros del proyecto.

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
    title: models.CharField(max_length=140) # Representa el título de la película
    plot: models.TextField()  # Permite agregar parrafos en este caso un argumento sobre la pelicula.
    year = models.PositiveIntegerField() # Indica el año de lanzamiento de la pelicula
    rating = models.IntegerField(choices=RATINGS, default=NOT_RATED) # Explicación
    website = models.URLField(blank=True)
    ```

2. Agregue el método `__str__` al modelo Movie.

3. Ejecute las migraciones.
    
    ````python
    python manage.py makemigrations core
    python manage.py migrate core
    ```
