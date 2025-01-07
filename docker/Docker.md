**Listar imagenes**
```
docker images
```

**Descargar imagen**
```
docker pull node
```

Por defecto descarga la **latest**, se puede especificar la version haciendo
```
docker pull node:18 
```

![[Pasted image 20241229141237.png]]

Para saber que imagenes descargar, ir a [DockerHub](https://hub.docker.com/)

**Eliminar imagen**
```
docker image rm <image-name>:<version>
```

**Crear un contenedor en base a una imagen**
```
docker create <image-name>
```
![[Pasted image 20241229141816.png]]
Devuelve el ID del contenedor creado. Este comando lo crea pero no lo ejecuta

**Iniciar contenedor**
```
docker start <container-id>
```
![[Pasted image 20241229142137.png]]

**Listar contenedores activos**
```
docker ps
```

**Listar todos los contenedores**
```
docker ps -a
```

**Parar un contenedor**
```
docker stop <container-id>
```

**Eliminar un contenedor**
```
docker rm {<container-id>|<container-name>}
```

**Crear un contenedor con nombre custom**
```
docker create --name <container-name> <image>
```
![[Pasted image 20241229142815.png]]
Aunque podemos ver que nos indica que el puerto **27017** es el que esta utilizando mongo, nosotros no vamos a poder comunicarnos con el contenedor porque no hay ningun puerto expuesto para hacerlo. Para eso hay que indicarle a docker que el puerto **27017** de nuestra maquina va a ser el puerto **27017** del contenedor (port mapping).
![[Pasted image 20241229143250.png]]


**Crear docker con mapeo de puertos**
```
docker create -p<host-port>:<container-port> --name monguito mongo

#Example
docker create -p27017:27017 --name monguito mongo
```
![[Pasted image 20241229143558.png]]

**Ver logs de un contenedor desplegado**
```
docker logs {<container-id>|<container-name>}
```

**Quedar escuchando los logs**
```
docker logs --follow {<container-id>|<container-name>}
```

**Combinacion de pull, create y start. Docker run**
```
docker run -d mongo
```
-d <--- detached. La consola no queda escuchando los logs
este comando
- Busca la imagen, si no existe la descarga
- Crea el contenedor
- Inicia el contenedor
```
docker run --name monguito -p27017:27017 -d mongo
```
![[Pasted image 20241230085350.png]]


Los contenedores ciertas configuraciones para que nosotros podamos conectarnos con ellos. En caso de un contenedor con la imagen de mongo requiere
```
`MONGO_INITDB_ROOT_USERNAME`, `MONGO_INITDB_ROOT_PASSWORD`
```
Esto puede verse en DockerHub

**Crear contenedor con envs**
```
docker create -p27017:27017 --name monguito -e MONGO_INITDB_ROOT_USERNAME=loow3 -e MONGO_INITDB_ROOT_PASSWORD=asdfj mongo
```
![[Pasted image 20241230092028.png]]

**Tomar una app y meterla dentro de un contenedor**
Lo primero es crear un archivo llamado **==Dockerfile==**
El Dockerfile se utiliza para crear el contenedor, aqui es donde definimos las instrucciones que tiene que seguir docker para crearlo correctamente

```Dockerfile
FROM node:18

RUN mkdir -d /home/app

COPY . /home/app

EXPOSE 3000

CMD ["node", "/home/app/index.js"]
```
- **`FROM node:18`**: Usa la imagen base oficial de Node.js versión 18.
- **`RUN mkdir -d /home/app`**: Crea el directorio `/home/app` dentro del contenedor.
- **`COPY . /home/app`**: Copia todos los archivos del proyecto al directorio `/home/app` dentro del contenedor.
- **`EXPOSE 3000`**: Expone el puerto 3000, indicando que la aplicación escuchará en este puerto.
- **`CMD ["node", "/home/app/index.js"]`**: Define el comando por defecto para iniciar la aplicación, ejecutando `index.js` con Node.js.


**Red entre contenedores**
Cuando creamos contenedores estos por defecto no pueden comunicarse entre si, pueden trabajar isolados entre ellos y exponer un puerto para que nosotros podamos comunicarnos con ellos.

Para que estos contenedores puedan comunicarse entre si, hay que definir una `red interna de docker`
![[Pasted image 20241230093937.png]]

**Docker network**

**Listar redes de docker**
```
docker network ls
```
![[Pasted image 20241230100643.png]]

**Crear red**
```
docker network create mired
```

**Eliminar red**
```
docker network rm mired
```

Para comunicarse entre si, los contenedores dentro de una misma red utilizan el nombre del contenedor, es decir, el nombre de dominio del contenedor es su mismo nombre

**Docker build**
Docker build sirve para ==crear una imagen en base a un archivo **Dockerfile**==
```
docker build -t <name>:<tag> <directory>

#Example
docker build -t miapp:1 .
```
![[Pasted image 20241230111435.png]]

**Crear un contenedor y asignarle red**
```
docker create -p27017:27017 --name monguito --network mired -e MONGO_INITDB_ROOT_USERNAME=loow3 -e MONGO_INITDB_ROOT_PASSWORD=asdfj mongo
```

**Crear contenedor con imagen generada con Dockerfile**
```
docker create -p3000:3000 -name chanchito --network mired miapp:1
```


# Docker compose
```yml
version: "1.0"
services:
  chanchito:
    build: .
    ports:
      - "3000:3000"
    links:
      - monguito
  monguito:
    image: mongo
    ports:
      - "27017:27017"
    environment:
      - MONGO_INITDB_ROOT_USERNAME=loow3
      - MONGO_INITDB_ROOT_PASSWORD=asdfj
    volumes:
      - mongo-data:/data/db
      # mysql -> /var/lib/mysql
      # postgres -> /var/lib/postgresql/data

volumes:
  mongo-data:

```
El archivo `docker-compose.yml` que se presenta configura una aplicación que utiliza dos servicios: una aplicación web llamada "chanchito" y una base de datos MongoDB denominada "monguito". Este archivo facilita la configuración y el despliegue de estos servicios de manera eficiente utilizando Docker.

En primer lugar, se especifica la versión del archivo de configuración, en este caso, la versión "1.0". Esta versión asegura que el formato de sintaxis sea compatible con la versión de Docker que se esté utilizando.

El servicio "chanchito" está configurado para construir una imagen Docker desde el directorio actual. Además, se mapea el puerto 3000 del contenedor al puerto 3000 de la máquina local, lo que permite acceder a la aplicación web a través del navegador en `localhost:3000`. También, se establece una relación de dependencia entre "chanchito" y "monguito" mediante la directiva `links`, lo que permite que "chanchito" pueda comunicarse con "monguito" (el servicio de MongoDB) a través de la red interna creada automáticamente por Docker.

Por otro lado, el servicio "monguito" utiliza la imagen oficial de MongoDB y expone el puerto 27017 (el puerto predeterminado para MongoDB) para permitir el acceso a la base de datos desde otros servicios o desde el host local. Se definen dos variables de entorno para inicializar MongoDB con un nombre de usuario y una contraseña predeterminados: `MONGO_INITDB_ROOT_USERNAME` y `MONGO_INITDB_ROOT_PASSWORD`. Además, se configura un volumen persistente llamado "mongo-data", que se asocia con la ruta `/data/db` dentro del contenedor. Este volumen es crucial para almacenar de manera persistente los datos de la base de datos, incluso cuando el contenedor se detenga o reinicie.

Finalmente, en la sección de volúmenes, se define el volumen "mongo-data", que es utilizado por el contenedor de MongoDB para asegurar que los datos de la base de datos sean almacenados de forma persistente y no se pierdan al reiniciar el contenedor. Esta configuración también incluye comentarios que sugieren cómo configurar volúmenes para otras bases de datos como MySQL o PostgreSQL, lo que facilita la adaptación del archivo a diferentes tecnologías.

Cuando se ejecuta el comando `docker-compose up`, Docker construye y levanta ambos contenedores, la aplicación web y la base de datos, asegurando que la configuración esté lista para ser utilizada. La comunicación entre los servicios se maneja de forma transparente a través de la red interna de Docker, lo que simplifica el proceso de configuración y despliegue de la aplicación.

Este archivo `docker-compose.yml` proporciona una forma sencilla y efectiva de gestionar múltiples contenedores Docker, permitiendo que la aplicación y la base de datos trabajen juntas de manera coordinada.

**Ejecutar docker-compose.yml**
Desde el directorio en el que esta el archivo `docker-compose.yml`
```
docker compose up
```

**Eliminar todo lo creado por docker compose**
Este comando elimina las imagenes y contenedores creados por ejecutar `docker compose up`
```
docker compose down
```
![[Pasted image 20241230114108.png]]

# Ambientes

Teniendo distintos ambientes (DEV y PROD por ejemplo) vamos a necesitar distintos `docker-compose.yml` y `Dockerfile` que contengan distintas configuraciones.

Para eso creamos
- `docker-componse-dev.yml`
- `Dockerfile.dev`

**Ejemplo de docker-compose y Dockerfile en entorno DEV**

docker-compose-dev.yml
```yml
version: "3.9"
services:
  chanchito:
    build:
      context: .
      dockerfile: Dockerfile.dev
    ports:
      - "3000:3000"
    links:
      - monguito
    volumes:
      - .:/home/app
  monguito:
    image: mongo
    ports:
      - "27017:27017"
    environment:
      - MONGO_INITDB_ROOT_USERNAME=loow3
      - MONGO_INITDB_ROOT_PASSWORD=asdfj
    volumes:
      - mongo-data:/data/db
      # mysql -> /var/lib/mysql
      # postgres -> /var/lib/postgresql/data

volumes:
  mongo-data:

```

Dockerfile.dev
```Dockerfile
FROM node:18

RUN npm i -g nodemon
RUN mkdir -p /home/app

WORKDIR /home/app

EXPOSE 3000

CMD ["nodemon", "index.js"]

```