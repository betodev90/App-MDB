# Sesión 8

## Fase de despliegue
Puesta en marcha un proyecto django en este caso utilizaremos Heroku que es un servidor de hosting open source hasta ciertas características pero para el fin académico es muy útil.

1. Ir a la web de Heroku [https://www.heroku.com/](https://www.heroku.com/).

2. Crear una cuenta en Heroku, guardar las credenciales es decir `email` y `password`.

2. Descargar el instalador de Heroku que se encuentra la siguiente ruta [https://devcenter.heroku.com/articles/heroku-cli](https://devcenter.heroku.com/articles/heroku-cli), para el sistema operativo requerido.

3. Recordar en windows, ejecutar el instalador en modo `Administrador`.

4. Una vez instalado Heroku en su sistema operativo, proceder abrir un terminal/cmd y ejecutar los siguientes pasos:
    
    ```
    heroku login
    Enter your Heroku credentials:
    Email: email@dominio.com
    Password: *************
    Logged in as email@dominio.com
    ```

5. Si el paso previo ha sido exitoso se puede continuar y realizar los siguientes cambios:

    * Actualizar `Pipfile.lock`
    * Crear fichero `Procfile`
    * Instalar `gunicorn` para que trabaje como web server
    * Realizar cambios en el fichero de configuración del proyecto `settings.py`

6. Debido que el server de heroku es compatible con la versión `3.6` de python en el fichero `Pipfile` hacer el cambio.
    
    ```
    # Pipfile
    ...
    [requires]
    python_version = "3.6"
    ```

7. A continuación ejecutar el comando:
    ```pipenv lock```

    Heroku realmente busca en nuestro archivo `Pipfile.lock` información sobre nuestro entorno virtual, por lo que agregamos la configuración de idioma aquí.

8. Crear archivo `Procfile` archivo especifico para deploy en Heroku.

9. En el archivo creado `Procfile` agregar la siguiente línea.
    ```web: gunicorn config.wsgi --log-file -```

    Esto indica que usemos el archivo existente para deploy `config.wsgi` con `gunicorn`, que es un servidor web para producción.

10. Instalar la librería `gunicorn`.
    
    ```python
    pipenv install gunicorn
    ```

## Deploy

Los pasos siguientes son configurar en Heroku.

1. Crear una aplicación en Heroku y `push` el código del proyecto.
    En el terminal donde se hizo el paso previo de ingreso de credenciales de heroku, moverse al path del proyecto y ejecutar el comando.
    `heroku create`

2. Como resultado debe general la URL disponible donde alojaremos el proyecto. Ej:
    
    ```
    (MYMDB-iw5zc0RB) bash-3.2$ heroku create
    Creating app... done, ⬢ pacific-woodland-70128
    https://pacific-woodland-70128.herokuapp.com/ | https://git.heroku.com/pacific-woodland-70128.git
    ```

3. En este paso se necesita agregar un `Hook` for enlazar git en Heroku. Para eso ingresamos el comando.

    ```
    heroku git:remote -a pacific-woodland-70128
    ```
    Destacar que `pacific-woodland-70128` es el nombre de la aplicación en Heroku, que genero automáticamente en el paso anterior.

4. Como resultado muesta:

    ```
    (MYMDB-iw5zc0RB) bash-3.2$ heroku git:remote -a pacific-woodland-70128
    set git remote heroku to https://git.heroku.com/pacific-woodland-70128.git
    ```

5. Deshabilitar en primera instancia los estáticos para optimizar la carga de los mismos.

    ```
    heroku config:set DISABLE_COLLECSTATIC=1
    ```

6. En este paso enviamos el codigo del repo a Heroku.

    ```
    git push heroku master
    ```

    Finalmente, debemos hacer que su aplicación Heroku en vivo. A medida que los sitios web crecen en tráfico, necesitan servicios adicionales de Heroku, pero para nuestro ejemplo básico, podemos usar el nivel más bajo, web = 1, que también es gratuito.

7. Comando:

    ```
    heroku ps:scale web=1
    ```
8. Para probar: `heroku open`

9. Para los estáticos, instalar la librería:

    ```
    pipenv install withenoise
    ```

10. Es necesario actualizar variables de configuración en el `settings.py`

    ```python
    ...
    INSTALLED_APPS = [
        'core',
        'users',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'whitenoise.runserver_nostatic', # Nuevo
        'django.contrib.staticfiles',
        
        # Third Packages 
        'crispy_forms',
    ]    
    ...
    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware', # Nuevo!
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]
    ...
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # Nuevo!
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage' # Nuevo
    ```

11. Para la configuración de base de datos con heroku ir al enlace [https://data.heroku.com/](https://data.heroku.com/).

12. Buscar la pestaña de Settings en la plataforma de Heroku.

13. Dar click en el menu de `Database Credentials`.

14. Cambiar la configuración en el setting.py variable `DATABASE`, en este ejemplo:
    
    ```python
    # Recordar que es un aleatorio que genera Heroku revisar las credenciales y hacer los cambios en DATABASES.
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'd5lri5hup9n5g4',
            'USER': 'ljteoysrgrwlty',
            'PASSWORD': '92f6885b84ebbb8c8787717eadb9719cffebe777eb1b2eae5121cc5f4ea5b1d8',
            'HOST': 'ec2-54-243-147-162.compute-1.amazonaws.com',  #'127.0.0.1',
            'PORT': '5432',
        }
    }   
    ```

15. Lo siguiente es ejecutar los comandos de migraciones.

    ```python
    heroku run python manage.py migrate
    # Para crear un superusario en la base de postgresql de Heroku
    heroku run python manage.py createsuperuser
    ```
