# MyMDB

## Descripción
Aplicación web que gestiona la información de películas.  

## Sesión 6

### Configuraciones y preparación del entorno de trabajo
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

### Aplicación Users
__Esta aplicación se encargará de la gestión de los usuarios que puedan acceder al proyecto web MyMDB__.

1. En `users/models.py` crear el modelo CustomUser con el campo `age` que tiene que ser  `PositiveIntegerField` y que herede de `AbstractUser`
2. Crear el fichero `forms.py` en el directorio de la aplicación `users`.
3. Crear dos formularios el primero para crear un usuario y el otro para modificar la información del mismo. Llamar a las clases `CustomUserCreateForm` y `CustomUserEditForm`.
    ```python
    from django import forms
    # Importar del core auth de django
    from django.contrib.auth.forms import UserCreationForm, UserChangeForm
    from .models import CustomUser
    ```
4. Agregar en `users/admin.py` la clase de `CustomUser` que hereda del core de django `UserAdmin`.

    ```python
    from django.contrib import admin
    from django.contrib.auth.admin import UserAdmin

    from .forms import CustomUserCreationForm, CustomUserChangeForm
    from .models import CustomUser

    class CustomUserAdmin(UserAdmin):
        add_form = CustomUserCreationForm
        form = CustomUserChangeForm
        list_display = ['email', 'username', 'age']
        model = CustomUser
    ```
5. Crear un superuser para que pueda acceder al AdminSite de Django.

__Procedimiento para la autenticación de los Usuarios al proyecto web (Login, Logout, Signup de usuarios)__

1. Crear un directorio templates/registration/, pero para que django lo encuentre se realiza la configuración en el settings.py variable `TEMPLATES`.

2. Segun el flujo cada vez que un usuario haga login o logout al sistema se configura la ruta a donde lo redirige después de estos eventos, esto se agrega en el settings.py. 
    ```python
    LOGIN_REDIRECT_URL = 'home'
    LOGOUT_REDIRECT_URL = 'home'
    ```
3. 

