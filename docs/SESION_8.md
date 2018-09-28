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