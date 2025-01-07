![[Pasted image 20241223095451.png]]

Funciones clave: 
- Enrutamiento: Recibe solicitudes de los clientes y las redirige al microservicio correspondiente en funcion de la ruta o el tipo de solicitud
- Seguridad: Gestiona autenticacion y autorizacion de los clientes
- Transformacion de datos: puede transformar o adaptar datos en tiempo real para que coincidan con los formatos esperados por los microservicios individuales, lo que facilita la integracion de diferentes sistemas y versiones de la API.
- Cache: puede implementar una capa de cache para almacenar en memoria las respuestas de los microservicios, mejorando la velocidad y reduciendo la carga en los servicios subyacentes.
- Control de trafico: permite gestionar el flujo de las solicitudes, aplicacndo limites y prioridades para garantizar u nrendimiento optimo y evitar asi la sobrecarga.

Para implementar API Gateway se puede hacer desde initializr con la dependecia **Gateway**