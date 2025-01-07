
Feign es una libreria en Java que proporciona una forma declarativa de definir y consumir sericio web REST.


# Feign vs RestTemplate

Sintaxis más clara y concisa para definir las llamadas a servicio REST. Además, se beneficia de la configuración y las características proporcionadas pro Spring Cloud. 


# Implementación paso a paso

## Paso 1

En initializr añadir OpenFeign

## Paso 2

definir estructura de paquetes clasica en la aplicación

## Paso 3

dentro del paquete DTO creamos una clase para recibir los datos que vamos a consultar de la Pokeapi.

```java
@Getter
@Seetter
@AllArgs
@NoArgs
public class PokemonDTO {
	private int id;
	private String name;
}
```

Esete DTO contiene los datos que vamos a filtrar de entre todos los que nos puede devolver la Poke AIP.

## Paso 4

En rl paquete repository vamos a llevar a cabo la creacion de una interfaz y lasa configuraciones necesarias para que nuestro repositorio sean los datos que vamos a consumir de cada Pokemon desde la Poke api. Esto lo vamos a hacer mediante una nueva annotation llamada @FeignClient y vamos a configurar la url que vamos a consumir, en esta ocacsion, la URL que nos proporciona la Poke API.

```java
@FeignClient(name = "pokeapi", url="https://pokeapi.co/api/v2")

public interface PokeAPIClient{
	@GetMapping("/pokemon/{pokemonId}")
	public PokemonDTO getPokemonInfo (@PathVariable ("pokemonId") int pokemonId); 
}
```

## Paso 5

Una vez creada nuestra interfaz, es necesario que establezcamos una configuracion en nuestro archivo application.properties
```
feign.pokeapi.url=https://pokeapi.co/api/v2
```

## Paso 6

Crear el controller

```java
@RestController
public class PokemonController{

	@Autowired
	privte PokeAPIClient pokeAPIClient;

	@GetMapping("/pokemon/{pokemonId}")
	public PokemonDTO getPokemonInfo(@PathVariable ("pokemonId") int pokemonId){
		return pokeAPIClient.getPokemonInfo(pokemonId);
	}
}
```

## Paso 7

Por ultimo, tenemos que establecer en nuestra clase Main la annotation @EnableFeignClients para permitir el uso correcto de Feign y ya estamos listos

```java
@SpringBootApplication
@EnableFeignClients
public class PokeapiApplication {
	public static void main(String[] args){
		SpingApplication.run(PokeapiApplication.class, args);
	}
}
```

# Paso 8

Pruebas en postman
![[Pasted image 20241219113801.png]]
