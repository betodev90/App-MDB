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

