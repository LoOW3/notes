## Ejemplo:

aplicacion para una red social que esta dividida en dos servicios: Posts y Users.

El servicio Users se encargara de gestionar la informacion de los usuarios de la red social, mientras que el servicio Posts las publicaciones que los mismo hacen en la plataforma.

El servicio Users debera consumir al servicio Posts para poder obtener todos los posteos que un determinado usuario haya escrito. 

### Paso 1
Crear el **Eureka-Server**

### Paso 2
Crear servicio Users y Posts con las siguientes dependencias

Users
![[Pasted image 20241222203722.png]]

Posts
![[Pasted image 20241222203805.png]]


### Paso 3
Crear configuraciones necesarias en application.properties
```
server.port=8083
spring.application.name=users-service

eureka.client.service-url.defaultZone=http://localhost:8761/eureka

spring.jpa.hibernate.ddl-auto=update
sping.datasource.url=jdbc:mysql://localhost:3306/users_service?serveTimezone=UTC
spring.datasource.username=loow3
spring.datasource.password=asdfj
spring.jpa.database-platform=org.hibernate.dialect.MySQL8Dialect
```

```
server.port=8082
spring.application.name=posts-service

eureka.client.service-url.defaultZone=http://localhost:8761/eureka

spring.jpa.hibernate.ddl-auto=update
sping.datasource.url=jdbc:mysql://localhost:3306/posts_service?serveTimezone=UTC
spring.datasource.username=loow3
spring.datasource.password=asdfj
spring.jpa.database-platform=org.hibernate.dialect.MySQL8Dialect
```