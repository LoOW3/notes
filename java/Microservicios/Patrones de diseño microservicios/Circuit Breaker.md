Cuando un microservicio intenta comunicarse con otro y experimenta fallas repetidas, el **Circuit braker** entra en accion. En lugar de permitir que las solicitudes fallidads se propaguen por el sistema, corta el circuito y deja de enviar solicitudes al servicio que posee problemas. En su lugar, se utiliza un flujo de datos alternativo, como por ejemplo, datos en cache o una respuesta predefinida, para mantener las funcionalidades basicas del sistema.![[Pasted image 20241223003836.png]]


Circuit breaked monitorea constantemente la disponibilidad del microservicio subyacente. Si detecta que el mismo ha recuperado su disponibilidad, El circuit Breaker abre el circuito nuevamente y permite que las solicitudes se envien normalmente



Para implementarlo se utiliza la libreria llamada **Netflix Hystrix**

Sin embargo en la actualidad la libreria **Resilience4j** se creo como una alternativa a Hystrix, que fue desarrollado originalmente por Netflix. Resilience4j se ha vuelto popular en la comunidad

## Implementacion

**Cirbuir Breakes con Resilience4j**

