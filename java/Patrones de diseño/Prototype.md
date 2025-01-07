Patrón de diseño creacional

**Prototype** es un patrón de diseño creacional que nos permite copiar objetos existentes sin que el código dependa de sus clases.

Tipos de clonación
- Clonación simple
	Clonamos el objeto pero no clonamos los objetos adyacentes con los que esté relacionado este objeto.
- Clonación profunda
	Clonamos sel objeto y los objetos adyacentes a este objeto.

![[Recording 20241021132751.webm]]
# Ejemplo
Main
```java
package org.example;  
  
import java.util.ArrayList;  
import java.util.List;  
  
public class Main {  
    public static void main(String[] args) {  
  
        List<Book> books = List.of(new Book("libro 1", "ignacio"),  
                new Book("libro 2", "Exequiel"),  
                new Book("libro 3", "Diaz"),  
                new Book("libro 4", "Nanni"));  
        Person person1 = new Person("Ignacio", "Diaz", books);  
  
        Person person2 = person1.deepClone();  
        System.out.println(person1.toString());  
        System.out.println(person2.toString());  
    }  
}
```

IPrototype
```java
package org.example;  
  
public interface IPrototype<T extends IPrototype> extends Cloneable {  
  
    public T clone();  
    public T deepClone();  
}
```

Person
```java
package org.example;  
  
import java.util.ArrayList;  
import java.util.List;  
  
public class Person implements IPrototype{  
  
    private String name;  
    private String lastName;  
    private List<Book> books;  
  
    public Person(String name, String lastName, List<Book> books) {  
        this.name = name;  
        this.lastName = lastName;  
        this.books = books;  
    }  
  
    public Person() {  
    }  
  
    public String getName() {  
        return name;  
    }  
  
    public void setName(String name) {  
        this.name = name;  
    }  
  
    public String getLastName() {  
        return lastName;  
    }  
  
    public void setLastName(String lastName) {  
        this.lastName = lastName;  
    }  
  
    public List<Book> getBooks() {  
        return books;  
    }  
  
    public void setBooks(List<Book> books) {  
        this.books = books;  
    }  
  
    @Override  
    public Person clone() {  
        return new Person(name, lastName, books);  
    }  
  
    @Override  
    public Person deepClone() {  
        Person person = new Person();  
        person.setName(name);  
        person.setLastName(lastName);  
        List<Book> booksClone = new ArrayList<>();  
        for(Book book: books){  
            Book bookClone = new Book(book.getName(), book.getAuthor());  
            booksClone.add(bookClone);  
        }  
        person.setBooks(booksClone);  
        return person;  
    }  
  
    @Override  
    public String toString() {  
        return Integer.toHexString(System.identityHashCode(this)) + " - Person{" +  
                "name='" + name + '\'' +  
                ", lastName='" + lastName + '\'' +  
                ", books=" + books +  
                '}';  
    }  
}
```

Book
```java
package org.example;  
  
public class Book implements IPrototype {  
    private String name;  
    private String author;  
  
    public Book(String name, String author) {  
        this.name = name;  
        this.author = author;  
    }  
  
    public Book() {  
    }  
  
    public String getName() {  
        return name;  
    }  
  
    public void setName(String name) {  
        this.name = name;  
    }  
  
    public String getAuthor() {  
        return author;  
    }  
  
    public void setAuthor(String author) {  
        this.author = author;  
    }  
  
    @Override  
    public Book clone() {  
        return new Book(name, author);  
    }  
  
    @Override  
    public Book deepClone() {  
        return this.clone();  
    }  
  
    @Override  
    public String toString() {  
        return Integer.toHexString(System.identityHashCode(this)) +" - Book{" +  
                "name='" + name + '\'' +  
                ", author='" + author + '\'' +  
                '}';  
    }  
}
```