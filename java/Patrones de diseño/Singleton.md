Patrón de diseño creacional

**Singleton** es un patrón de diseño **creacional** que nos permite asegurarnos de que una clase tenga una única instancia, a la vez que proporciona un punto de acceso global a dicha instancia.

Tres reglas para implemetar un Singleton

- Debemos tener un constructor privado
- Debemos tener un atributo provado    estatico
- Debemos tener un metodo estatico que devuelva la instancia

```java
public class DataBaseConnector {
    private static DataBaseConnector instancia;
    private String url;

    // Constructor privado para evitar instanciación externa
    private DataBaseConnector() {
        this.url = "jdbc:mysql://localhost:3306/mi_base_de_datos";
    }
    // Método para obtener la instancia única
    public static synchronized DataBaseConnector getInstancia() {
        if (instancia == null) {
            instancia = new DataBaseConnector();
        }
        return instancia;
    }

    // Método para simular conexión
    public void conectar() {
        System.out.println("Conectado a la base de datos en: " + url);
    }

    // Método para simular desconexión
    public void desconectar() {
        System.out.println("Desconectado de la base de datos.");
    }
}

```

```java
public class Main {
    public static void main(String[] args) {
        // Obtén la instancia única de DataBaseConnector
        DataBaseConnector dbConnector = DataBaseConnector.getInstancia();
        
        // Conectar a la base de datos
        dbConnector.conectar();


        // Desconectar de la base de datos
        dbConnector.desconectar();
    }
}

```

## Usos
El patrón Singleton es útil en varias situaciones donde necesitas garantizar que una clase tenga una única instancia. Aquí hay algunas aplicaciones comunes:

1. **Control de acceso a recursos compartidos**: Por ejemplo, si tienes una conexión a una base de datos, quieres asegurarte de que solo haya una conexión activa.
    
2. **Configuraciones globales**: Puedes usar un Singleton para manejar configuraciones de la aplicación que deben ser accesibles desde diferentes partes de tu código.
    
3. **Gestión de logs**: Un logger puede ser implementado como un Singleton para asegurar que todas las partes de la aplicación escriban en el mismo archivo o sistema de logging.