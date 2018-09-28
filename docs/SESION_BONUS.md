# Legacy Database

1. Ir a  [http://www.postgresqltutorial.com/load-postgresql-sample-database/](http://www.postgresqltutorial.com/load-postgresql-sample-database/)

2. Comando que se debe ejecutar, una vez configurado el proyecto en django.
    ```python
        python manage.py inspectdb > models.py
    ```

# RESTful con Django
3. Para trabajar con una API REST en Django se requiere el apoyo de la librería `django-rest-framework`

4. Una vez instalada agregar al `settings.py` en `INSTALLED_APPS`.

5. Crear en la aplicación `core` un fichero `serializers.py`
    ```python
    from rest_framework import serializers
    from .models import Movie

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            # fields = ()
    ```

6. Agregar una vista `core` en el fichero `views.py`

    ```python
    from rest_framework import viewsets
    from .models import Movie
    from .serializers import MovieSerializer

    class MovieViewSet(viewsets.ModelViewSet):
        queryset = Movie.objects.all()
        serializer_class = MovieSerializer
    ```

7. Configurar las `urls.py`.

    ```python
        from django.conf.urls import url
        from rest_framework import routers
        from .views import MovieViewSet

        router = routers.DefaultRouter()
        router.register(r'api/movies', MovieViewSet)

        urlpatterns = router.urls
    ```
