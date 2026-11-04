# Mi Proyecto Automotriz - Evaluación Sumativa 3

## Propósito y Proyección

Este proyecto es una aplicación backend funcional desarrollada en Django, conectada a una base de datos PostgreSQL. Permite gestionar un catálogo automotriz utilizando operaciones CRUD, validaciones de seguridad y administración desde el panel de Django.

## Integrante

- Benjamin Millalonco

## Requisitos e Instalación (Para el evaluador)

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/hxcCoder/Evaluacion-sumativa-3.git
   ```

2. Entrar a la carpeta del proyecto:

   ```bash
   cd evaluacion-sumativa-3
   ```

3. Crear y activar el entorno virtual:

   - **Windows:**
     ```bash
     python -m venv .venv
     .venv\Scripts\activate
     ```

   - **Mac/Linux:**
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

4. Instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

## Configuración de Base de Datos y Variables de Entorno

1. Crear una base de datos vacía en PostgreSQL.

2. Copiar el archivo `.env.example` y renombrarlo a `.env`.

3. Abrir el archivo `.env` y completar los datos con las credenciales locales de PostgreSQL:

   ```env
   SECRET_KEY=tu_secret_key
   DEBUG=True
   DB_NAME=tu_base_de_datos
   DB_USER=tu_usuario
   DB_PASSWORD=tu_password
   DB_HOST=localhost
   DB_PORT=5432
   ```

4. Aplicar las migraciones para crear las tablas:

   ```bash
   python manage.py migrate
   ```

5. Crear un superusuario para acceder al panel administrativo:

   ```bash
   python manage.py createsuperuser
   ```

6. Ejecutar el servidor:

   ```bash
   python manage.py runserver
   ```

## Estructura del Proyecto

- **core:** Contiene las rutas generales y vistas estáticas.
- **Autos:** Implementa el CRUD de vehículos, con conexión a base de datos, validaciones y formularios web.
- **Precios:** Contiene el listado estático de precios de servicios.

---

## Usuarios de Prueba para Evaluación

Para probar los endpoints protegidos de la API REST mediante Postman o Insomnia:

- **Usuario de prueba:** `admin_api` o cualquier usuario creado mediante `createsuperuser`.
- **Contraseña:** Definida localmente al ejecutar `createsuperuser`.

No se incluyen contraseñas reales en el repositorio.

---

## Estructura de Endpoints de la API REST

### Autenticación JWT

| Método | Ruta | Propósito | Protección |
|---|---|---|---|
| **POST** | `/api/token/` | Obtener tokens `access` y `refresh` | Pública |
| **POST** | `/api/token/refresh/` | Renovar el token de acceso vencido | Pública |

### Recurso Principal: Vehículos (`/api/autos/`)

| Método | Ruta de referencia | Propósito | Protección |
|---|---|---|---|
| **GET** | `/api/autos/` | Listar todos los vehículos del catálogo | Pública |
| **GET** | `/api/autos/<id>/` | Consultar el detalle de un vehículo específico | JWT Obligatorio |
| **POST** | `/api/autos/` | Registrar un nuevo vehículo | JWT Obligatorio |
| **PUT** | `/api/autos/<id>/` | Actualizar un vehículo existente | JWT Obligatorio |
| **DELETE** | `/api/autos/<id>/` | Eliminar un vehículo del catálogo | JWT Obligatorio |

### Nota de Seguridad

Las solicitudes protegidas requieren el envío del token de acceso en el encabezado HTTP de la petición:

```http
Authorization: Bearer <tu_access_token>
```

---

## Validación y Pruebas de la API REST

Las pruebas de los endpoints fueron realizadas utilizando Postman, verificando el funcionamiento de las operaciones CRUD y la autenticación mediante JWT.

Se realizaron las siguientes pruebas:

- Obtener token JWT mediante `/api/token/`.
- Consultar listado de vehículos mediante GET sin autenticación.
- Consultar detalle de vehículo mediante GET con token JWT.
- Crear vehículo mediante POST con token JWT.
- Actualizar vehículo mediante PUT con token JWT.
- Eliminar vehículo mediante DELETE con token JWT.
- Verificar rechazo de solicitudes POST sin autenticación.
- Verificar rechazo de datos inválidos durante la creación de vehículos.

## Verificación de Base de Datos

Se comprobó la persistencia de los registros mediante PostgreSQL y el panel administrativo de Django (`/admin/`), verificando que las operaciones realizadas desde la API se reflejen correctamente en la base de datos.

## Tecnologías Utilizadas

- Python
- Django
- Django REST Framework
- PostgreSQL
- Simple JWT
- Postman

## Documentación y Evidencias

Se incluyen evidencias en el informe de evaluación, mediante capturas de pantalla de las pruebas realizadas en Postman, configuración del proyecto, autenticación JWT y verificación de registros en PostgreSQL y Django Admin.

## Consideraciones de Seguridad

- Las credenciales de base de datos se configuran mediante variables de entorno.
- El archivo `.env` no debe subirse al repositorio.
- Las operaciones de escritura y modificación de vehículos requieren autenticación JWT.
- Se recomienda utilizar una clave secreta segura en ambientes de producción.