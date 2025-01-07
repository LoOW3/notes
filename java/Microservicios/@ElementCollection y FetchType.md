# @ElementCollection

La anotacion elementCollection en java se utiliza en el consexto de mapeo objeto-relacional (ORM) para indicar que una coleccion de valores simplres (como String, Integer, etc) debe ser mapeada y persistida en una tabla separada.

Supongamos que tenes una clase llamada Usuario que tiene una coleccion de numeros de telefono. En lugar de crear una clase separada de estos, podes usar @ElementCollection para mapearlos como parte de la entidad Usuario.

```java
@Entity
public class Usuario {
@Id
@geneeratedValue(strategy = GenerationType.IDENTITY)
private Long id;
private String nombre;
@elementCollection
private List<String> numerosDeTelefono;
}
```

# FetchType

## Lazy
los datos se cargan solamente cuando los necesites 
Mayor rendimiento

```java
@Entity public class Pedido {
@id
private Long id;

@OneToMany(fetch = FetchType.LAZY)
private List<ItemPedido> items;
}
```

## EAGER

carga todo
```java
@Entity public class Pedido {
@id
private Long id;

@OneToMany(fetch = FetchType.EAGER)
private List<ItemPedido> items;
}
```