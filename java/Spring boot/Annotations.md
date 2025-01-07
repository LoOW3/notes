# @Column

- name
	se usa para especificar el nombre que queremos que tenga la tabla en la DB
- length
	cantidad de caracteres que quiero que tenga el campo como maximo.
- nullable (default **true**)
	si permito que el campo sea o no nulo.
- unique (default **false**)
	si permito que el valor del campo este o no repetido.
- insertable (default **true**)
	permito que se puedan insertar datos o no.
- updatable (default **true**)
	permito que una vez creado el registro pueda actualizar este campo
- columnDefinition
	Tipo de dato que va a tener en SQL
	- VARCHAR(300)
	- DATE
	- etc...

# @JoinTable
- name