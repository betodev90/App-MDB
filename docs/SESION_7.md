# Sesión 7

### Para continuar
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

### Agregando librerías de terceros

## Agregando características en la aplicación `users`

1. Elegiremos el paquete de terceros `django-crispy-forms`, para agregarlo a los formularios. Para esto utilizar pipenv para instalar el paquete al proyecto.
    ```python
    pipenv install django-crispy-forms
    ```
2. Agregar al settings.py en la variable `INSTALLED_APPS`.

3. Configure y agregue la siguiente variable de configuración en el `settings.py`.
    ```python
    CRISPY_TEMPLATE_PACK = 'bootstrap4'
    ```

4. Editar el archivo html `templates/signup.html` especificamente cargue la librería en el template.
    ```
    {% extends 'base.html' %}
    {% load crispy_forms_tags %}
    ...
    ```
