**Ejecutar comandos en un contenedor activo**
```
docker exec -it <container-name>
```
```
#Ejemplo
docker exec -it mysql-container mysql -u root -p
```
![[Pasted image 20250102105301.png]]


**Borrar todos los contenedores**
```
docker rm $(docker ps -aq)
```

**Borrar todas las imagenes**
```
docker rmi $(docker images -q)
```
