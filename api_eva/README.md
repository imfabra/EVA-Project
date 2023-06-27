# Instrucciones para probar el proyecto

A continuación se detallan los pasos necesarios para iniciar el proyecto y probarlo en tu entorno local.

## Requisitos previos
- Asegúrate de tener instalado Redis en tu sistema. Puedes instalarlo ejecutando el siguiente comando:
```
brew install redis
```


## Pasos a seguir

1. **Iniciar el servidor Redis:**
 - Abre una terminal y ejecuta el siguiente comando:
   ```
   redis-server
   ```
 - Esto iniciará el servidor Redis en el puerto predeterminado (6379) en tu máquina local.

2. **Iniciar el worker de Celery:**
 - Abre otra terminal y navega hasta el directorio raíz de tu proyecto Django.
 - Ejecuta el siguiente comando para iniciar el worker de Celery:
   ```
   celery -A tuprojecto worker --loglevel=info
   ```
   Asegúrate de reemplazar `'tuprojecto'` por el nombre correcto de tu proyecto Django.

3. **Iniciar el servidor de desarrollo de Django:**
 - En la misma terminal donde iniciaste el worker de Celery, ejecuta el siguiente comando para iniciar el servidor de desarrollo de Django:
   ```
   python manage.py runserver
   ```
 - Esto iniciará el servidor de desarrollo de Django y podrás acceder a tu proyecto en `http://localhost:8000` (o en la dirección que se muestre en la terminal).

Con estos pasos, Redis, Celery y Django estarán funcionando en tu entorno local. Ahora puedes probar y explorar el proyecto en tu navegador web.

¡Disfruta probando el proyecto!


## Detener los servicios

1. **Detener el worker de Celery:**
   - Regresa a la terminal donde se inició el worker de Celery.
   - Presiona `Ctrl + C` para detener la ejecución del worker.

2. **Detener el servidor de desarrollo de Django:**
   - Regresa a la terminal donde se inició el servidor de desarrollo de Django.
   - Presiona `Ctrl + C` para detener el servidor.

3. **Detener el servidor Redis:**
   - En la terminal donde se está ejecutando el servidor Redis, presiona `Ctrl + C` para cerrar la instancia del servidor.

Recuerda finalizar correctamente los servicios para evitar problemas y liberar recursos en tu entorno de desarrollo.

Si deseas volver a ejecutar el proyecto en el futuro, simplemente sigue los pasos proporcionados anteriormente para iniciar Redis, Celery y Django según sea necesario.


## Equipo

Este proyecto esta siendo desarrollado por el equipo de HDI. miembros del equipo:

- Daniel Fabra (@imfabra)
- David Henao (@)
- Cristian Roa (@)
- Alexander Carvajal (@)
