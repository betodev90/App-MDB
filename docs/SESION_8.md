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

5. Si el paso previo ha sido exitoso se puede continuar. Se debe realizar los cambios en:

    * Actualizar `Pipfile.lock`
    * Crear fichero `Procfile`
    * Instalar `gunicorn` para que trabaje como web server
    * Realizar cambios en el fichero de configuración del proyecto `settings.py`