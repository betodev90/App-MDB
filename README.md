# MyMDB

## Descripción
Aplicación web que gestiona la información de películas.  

### Sesión 6
1. Clonar el repositorio en un directorio de su máquina local
2. Verificar al clonar el repositorio que se tenga los ficheros Pipfile y Pipfile.lock correspondiente a su versión de python, si no es así modificar los ficheros.
3. Activar el entorno virtual con el comando.
    `pipenv shell`
4. Verificar que se instale django si no proceda a instalar en su virtualenv django con el comando revisado en clase.
    `pipenv install django`
5. Crear un proyecto en django llamado config de la siguiente manera:
    `django-admin.py startproject config .` ó `django-admin.exe startproject config`
6. Realizar la configuración de la base de datos en el fichero settings.py utilizar la configuración de postgres:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'mymdb',
            'USER': 'mymdb',
            'PASSWORD': 'development',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }       
    ```

7. Crear las siguientes aplicaciones core, users.
8. Agregar en el settings.py las aplicaciones creadas en el paso anterior.
9. En el settings.py agregar una variable `AUTH_USER_MODEL= 'users.CustomUser`.
10. En `users/models.py` crear el modelo CustomUser con el campo `age` y que herede de `AbstractUser`