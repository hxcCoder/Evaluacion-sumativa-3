Descripción del Problema / Objetivo:
Garantizar la seguridad en las operaciones de escritura (POST) de la API REST de la aplicación Autos, restringiendo la creación de recursos únicamente a usuarios autenticados, mientras se permite la lectura pública (GET).

2Prompt / Consulta enviada a la IA:

"¿Cómo puedo proteger el método POST en mis vistas de Django REST Framework para que solo los usuarios autenticados puedan crear vehículos, pero manteniendo el GET público?"

3Respuesta de la Inteligencia Artificial:
La IA indicó la implementación del decorador @permission_classes de Django REST Framework junto con la clase IsAuthenticatedOrReadOnly en el archivo Autos/views.py:


"from rest_framework.permissions import IsAuthenticatedOrReadOnly"

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def auto_list(request):
    
4. Análisis Técnico del Desarrollador:
La solución sugerida es adecuada y eficiente para este caso de uso. Al aplicar la clase de permiso IsAuthenticatedOrReadOnly, Django REST Framework restringe los métodos de modificación (POST, PUT, DELETE) a peticiones con token JWT válido, manteniendo el acceso anónimo y seguro para peticiones de lectura (GET).

5. Verificación y Resultado:
Se importó la clase de permisos y se agregó el decorador @permission_classes([IsAuthenticatedOrReadOnly]) sobre la vista del API. Al probar la vista con Postman, se confirmó que las solicitudes GET responden con código 200 OK sin credenciales, mientras que las solicitudes POST no autenticadas devuelven un código 401 Unauthorized.

6. Reflexión / Aprendizaje:
La arquitectura modular de decoradores en DRF facilita la aplicación de políticas de seguridad granulares por endpoint, permitiendo separar la lógica de negocio de las reglas de autorización del sistema.