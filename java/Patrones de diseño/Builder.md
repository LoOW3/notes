**Builder** es un patrón de diseño creacional que nos permite construir objetos complejos paso a paso.

El patrón nos permite producir distintos tipos y representaciones de un objeto empleando el mismo código de construcción. 

Ejemplo: 

Metodo builder implementado a la creacion de empleados

```java
package org.example;  
  
import java.util.ArrayList;  
import java.util.List;  
  
public class Employee {  
    private String name;  
    private String job;  
    private List<Contact> contactList;  
  
    // Constructor privado para usar con el Builder  
    private Employee(String job, String name, List<Contact> contactList) {  
        this.job = job;  
        this.name = name;  
        this.contactList = contactList; // Asignar la lista de contactos  
    }  
  
    public static class EmployeeBuilder implements IBuilder<Employee> {  
        private String name;  
        private String job;  
        private List<Contact> contactList = new ArrayList<>();  
  
        public EmployeeBuilder() {}  
  
        public EmployeeBuilder setName(String name) {  
            this.name = name;  
            return this;  
        }  
  
        public EmployeeBuilder setJob(String job) {  
            this.job = job;  
            return this;  
        }  
  
        public EmployeeBuilder addContact(Contact contact) {  
            this.contactList.add(contact);  
            return this;  
        }  
  
        public EmployeeBuilder addContact(String name, String phone) {  
            this.contactList.add(new Contact(name, phone));  
            return this;  
        }  
  
        @Override  
        public Employee build() {  
            return new Employee(job, name, contactList);  
        }  
    }  
  
    public String getName() {  
        return name;  
    }  
  
    public String getJob() {  
        return job;  
    }  
  
    public List<Contact> getContactList() {  
        return contactList;  
    }  
  
    @Override  
    public String toString() {  
        return "Employee{" +  
                "name='" + name + '\'' +  
                ", job='" + job + '\'' +  
                ", contactList=" + contactList +  
                '}';  
    }  
}
```

```java
package org.example;  
  
public interface IBuilder<T> {  
    public T build();  
}
```

```java
package org.example;  
  
public class Contact {  
    public String name;  
    public String phone;  
  
    public Contact(String phone, String name) {  
        this.phone = phone;  
        this.name = name;  
    }  
  
    public Contact() {  
    }  
  
    public String getName() {  
        return name;  
    }  
  
    public void setName(String name) {  
        this.name = name;  
    }  
  
    public String getPhone() {  
        return phone;  
    }  
  
    public void setPhone(String phone) {  
        this.phone = phone;  
    }  
  
    @Override  
    public String toString() {  
        return "Contact{" +  
                "name='" + name + '\'' +  
                ", phone='" + phone + '\'' +  
                '}';  
    }  
}
```

```java
package org.example;  
  
public class Main {  
    public static void main(String[] args) {  
        Employee employee = new Employee.EmployeeBuilder()  
                .setName("John Doe")  
                .setJob("Developer")  
                .addContact("Jane Doe", "123456789")  
                .addContact(new Contact("John Smith", "987654321"))  
                .build();  
  
        System.out.println(employee);  
    }  
}
```