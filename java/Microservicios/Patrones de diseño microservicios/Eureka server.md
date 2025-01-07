Eureka Server es una tecnologia utiliaza para el registro y descubrimiento de servicios en entornos de microservicios.

# Implementación

Agregar Eureka serve al paquete de Initializr

En la clase main, colocar **@EnableEurekaServer**

en **application.properties**:
- spring.application.name=eureka-server
- server.port=8761
- eureka.client.register-with-eureka=false
- eureka.client.fetch-registry=false
- eureka.instance.lease-renewal-interval-in-seconds=0

spring.application.name sirve para establecer el nombre de una determinada aplicacion de Spring boot.

server.port puerto en el que corre.

eureka.client.register-with-eureka establece al cliente eureka si debe registrarse automaticamente en Eureka Server o no. Si se establece en false, la aplicacion no se registrara, es decir, no estara visible para otros servicios.

eureka.client.fetch-registry indica al cliente Eureka si debe obtener el registro de servicios desde eureka server.


# Registrar servicios en Eureka Server

en Initializr agregar **Eureka Discovery Client** y **Spring Boot Actuator**

Eureka discovery Client permite que tu microservicio se registre automaticamente en el servidor Eureka cuando se inicia.

Spring Boot Actuator proporciona endpoints de monitoreo y gestion para tu aplicacion Spring Boot, lo que facilita la supervision y el mantenimiento en produccion.

application.properties 
```
server.port = 8081
spring.application.name=meter-converter

eureka.client.service-url.defaultZone=http://localhost:8761/eureka
```

En la clase main agregar el annotation @EnableDiscoveryClient