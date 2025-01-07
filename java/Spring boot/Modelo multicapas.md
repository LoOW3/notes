```
app/
	service/
	repository/
	dto/
	model/
	controller/
```

En el paquete de service se alojan lso metodos que se utilizaran para, por ejemplo, listar objetos de la base de datos, metodos para filtrarlos, etc.

El repository es un lugar donde se realiza el almacenamiento, manejo o administracion de los datos con los que trabajar la aplicacion, sea una base de datos, un archivo, etc.

en dto esta el modelado de como queremos devolver la informacion en la response, basado en la clases que tengamos definidas.

En model estan las clases (ej persona, propiedad, barrio, etc)

En controller esta el controlador que permite la interaccion con el API.


# Injecciones

teniendo
```
repository/
service/
controller/
```

en service se injecta con 
```
@Autowired
private IPersonaReposity pR;
```

y en el controller se injecta el interface del service
```
@Autowired
private IPersonaService pS;
```
