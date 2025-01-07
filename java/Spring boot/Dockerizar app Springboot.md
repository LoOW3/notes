tener la app funcionando en local

Crear el Dockerfile en la raiz

```
FROM openjdk:17-jdk-slim
ARG JAR_FILE=target/clinica_veterinaria-0.0.1.jar
COPY ${JAR_FILE} app_veterinaria.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app_veterinaria.jar"]
```
- **FROM openjdk:17-jdk-slim**:
    
    - Este comando especifica la imagen base para el contenedor. En este caso, se está utilizando una imagen de OpenJDK 17 en su versión "slim", que es más ligera y contiene solo lo esencial para ejecutar aplicaciones Java.
- **ARG JAR_FILE=target/clinica_veterinaria-0.0.1.jar**:
    
    - Aquí se define una variable de construcción llamada `JAR_FILE`. Su valor predeterminado es la ruta del archivo JAR que se quiere copiar al contenedor. Esta variable puede ser sobrescrita al construir la imagen si es necesario.
- **COPY ${JAR_FILE} app_veterinaria.jar**:
    
    - Este comando copia el archivo JAR desde el contexto de construcción (tu máquina local o el directorio donde se ejecuta el comando de construcción) al sistema de archivos del contenedor, renombrándolo a `app_veterinaria.jar`.
- **EXPOSE 8080**:
    
    - Este comando indica que el contenedor escuchará en el puerto 8080. Esto es importante para la configuración de red, pero no abre el puerto; solo documenta que la aplicación usará ese puerto.
- **ENTRYPOINT ["java", "-jar", "app_veterinaria.jar"]**:
    
    - Este comando establece el punto de entrada del contenedor. Cuando se inicie el contenedor, ejecutará el comando `java -jar app_veterinaria.jar`, que inicia la aplicación Java contenida en el archivo JAR.


```
version: '3'

services:
  app_vet:
    build: clinica_veterinaria
    mem_limit: 512m
    ports:
      - "8080:8080"
    environment:
      DB_URL: jdbc:mysql://clinica_vet:3306/clinica_veterinaria?createDatabaseIfNotExist=true&serverTimezone=UTC
      DB_USER_NAME: root
      DB_PASSWORD: 1234
    restart: always
    depends_on:
      clinica_vet:
          condition: service_healthy
  clinica_vet:
    image: mysql:8.0.33 
    ports:
      - "3307:3306"
    environment:
      MYSQL_ROOT_PASSWORD: 1234
      MYSQL_PASSWORD: 1234
      MYSQL_DATABASE: clinica_veterinaria
    restart: always
    healthcheck:
      test: ["CMD", "mysqladmin" ,"ping", "-h", "localhost"]
      timeout: 10s
      retries: 10
```

Setear variables de entorno en Intellij 

![[Pasted image 20241015163650.png]]

![[Pasted image 20241015163706.png]]