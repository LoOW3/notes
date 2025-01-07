# OneToOne

Cuando tengo una relacion de uno a uno lo que tengo que hacer es crear una clave foranea en una de las tablas
Cual debe tener la clave foranea? Depende de la logica de negocio de la aplicacion

Donde se quiera hacer la relacion
```java
public class Club{
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long id;
	private String name;
	@OneToOne(targetEntity = Coach.class, cascade = CascadeType.PERSIST )
	private Coach coach;
	
}
```

Se puede personalizar el nobre de la tabla de la clave foranea con 
```java

public class Club{
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long id;
	private String name;
	@OneToOne(targetEntity = Coach.class, cascade = CascadeType.PERSIST )
	@JoinColumn(name = "id_coach")
	private Coach coach;
	
}
```
## cascade 
Tiene muchos tipos.

Lo que determina es el comportamiento que va a seguir la relacion en caso de que se edite, borre, etc la tabla "Club".
Por ejemplo si se borra el club, puede borrarse tambien el coach asociado con un  CascadeType.REMOVE.

### ESTUDIAR CASCADE TYPES

# OneToMany

Ejemplo un club tiene muchos jugadores pero un jugador solo tiene un club

Para una relacion de uno a muchos se crea una clave foranea del lado del muchos.



```java
public class Player{
	@Id
	@GeneratedValue( strategy = GenerationType.IDENTITY)
	private Long id;
	private String name;
	@Column(name = "last_name");
	private String lastName;
	private String position;

	@ManyToOne(targetEntity = Club.class)
	private Club club;
}
```

```java
public class Club{
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long id;
	private String name;
	@OneToOne(targetEntity = Coach.class, cascade = CascadeType.PERSIST )
	private Coach coach;

	@OneToMany(targetEntity = Player.class, fetch = FetchType.LAZY, mappedBy = "club")
	private List<Player> players;
	
}
```

## mappedBy
Para lograr que del lado del Muchos se especifique el id de la entidad de Uno, se debe utilizar el mappedBy y especificar el nombre del campo que tiene en la entiedad del Muchos.
## fetch

FetchType.EAGER
	Cuando cargue un club me va a traer todos los jugadores directamente. A veces no necesito los players. Mas consumo de recursos innecesarios.
	
FetchType.LAZY
	cuando cargue un club me va a obtener los jugadores solo cuando se los pida yo. por ejemplo cuando yo haga uso del metodo getPlayers()

# @ManyToMany

```java
public class Club{
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long id;
	private String name;
	@OneToOne(targetEntity = Coach.class, cascade = CascadeType.PERSIST )
	private Coach coach;

	@OneToMany(targetEntity = Player.class, fetch = FetchType.LAZY, mappedBy = "club")
	private List<Player> players;


	@ManyToMany(targetEntity = FootballCompetition.class, fetch = FetchType.LAZY)
	@JoinTable(name = "club_competitions", joinColumns = @JoinColumn(name = "club"), inverseJoinColumns = @JoinColumn(name = "competition"))
	private List<FootballCompetition> footballCompetitions;
}
```

```java
public class FootballCompetition{
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long id;
	private String name;
}
```

Si se pone la relacion manytomany en las dos clases se crean dos tablas de intermedias.

