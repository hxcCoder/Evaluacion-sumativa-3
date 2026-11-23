Paso 1. Crear el superusuario
En PowerShell, ejecuta:
python manage.py createsuperuser


Completa:
- Username: el usuario que quieras.
- Email: tu correo (si lo solicita).
- Password: una contraseña que recuerdes.
Este usuario será el que utilizaremos para obtener el JWT.
Paso 2. Levantar el servidor
python manage.py runserver


Deberías ver:
Starting development server at http://127.0.0.1:8000/


No cierres esa terminal.
Paso 3. Comprobar Django Admin
Abre el navegador:
Django AdminInicia sesión con el superusuario que acabas de crear.

Comprueba que aparece la aplicación de automóviles y que puedes acceder a ella.
Paso 4. Probar la API con Postman
Primera prueba: GET público
MÉTODO GET
http://127.0.0.1:8000/api/autos/


Resultado esperado: 200 OK.

Después prueba la autenticación.

MÉTODO POST
http://127.0.0.1:8000/api/token/


Body → raw → JSON:
{
  "username": "TU_USUARIO",
  "password": "TU_PASSWORD"
}


Deberías recibir:
{
  "refresh": "...",
  "access": "..."
}


Ese access es tu JWT.
Paso 5. Demostrar el CRUD
En Postman utiliza:
Operación	Método	Endpoint
Listar	GET	/api/autos/
Crear	POST	/api/autos/
Consultar	GET	/api/autos/1/
Modificar	PUT	/api/autos/1/
Eliminar	DELETE	/api/autos/1/

Para POST, PUT, GET de detalle y DELETE, configura el token según los permisos de cada endpoint. En tu implementación, el listado permite GET público y el detalle requiere autenticación.

Importante: utiliza un ID que realmente exista al probar GET, PUT y DELETE.

Orden recomendado para tu defensa
1. Mostrar el listado de automóviles.
2. Obtener un JWT.
3. Crear un automóvil.
4. Consultar el automóvil creado.
5. Modificarlo con PUT.
6. Eliminarlo.
7. Mostrar que los datos se persisten en PostgreSQL mediante Supabase.
Siguiente paso: ejecuta createsuperuser y después runserver. Si aparece algún error, compárteme el mensaje exacto antes de continuar.