
Localmente tenemos dos servicios corriendo en distintos puertos, cada uno con sus tablas, models,controllers,services y reposity.

Para poder hacer consulta de uno a otro se utiliza la clase **RestTemplate** que la instancio en la clase AppConfig

```java
@Configuration
public class AppConfig {
	@Bean("apiConsumir")
	public RestTemplate registrarRestTemplate(){
		return new RestTemplate();
	}
}
```


En el service inyecto la instancia de RestTemplate en el Service
```java
@Autowired
private REstTemplate apiConsumir;
```



Para definir un metodo por fuera de JPA, en el Repository puedo definir queries SQL o HQL
```java
@Repository
public interface IPacienteRRepository extends JpaRepository<Paciente, Long>{
	@Query("SELECT p FROM Paciente p WHERE p.dni = :dni)
	Paciente findByDNI(String dni);
}
```


Para Obtener el Paciente por el DNI desde el otro microservicio en el service 
```java
Paciente pac = apiConsumir.getForObject("http://localhost:9001/pacientes/traerdni/" + dniPaciente, Paciente.class)
```