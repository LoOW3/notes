
### Volver atrás después de hacer un commit (local)

Si se quiere volver atrás despues de 
```
git add .
git commit -m ''
```

y mantener los cambios que se hicieron en **staging** se debe volver al commit anterior al nuestro utilizando
```
git reset --mixed <identificador>
```

![[git_1.png]]

en este caso para tener los cambios en staging del comit hecho el 19 de agosto debo volver al anterior 

```
git reset --mixed aab981ca83ef6646e1fe6d011bf92030f0acbb9c
```

