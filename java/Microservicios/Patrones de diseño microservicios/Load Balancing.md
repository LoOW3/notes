![[Pasted image 20241222201719.png]]

Balanceo de carga es fundamental en una arquitectura de microservicios por varias razones:

- **Escalabilidad y rendimiento**: En una arquitectura de microservicios, cada uno se ejecuta de manera independiente y puede tener multiples instancias en direrentes servidores. El balanceo de carga distribuye el trabajo entre las instancias, lo que perminte escalar horizontalmente y manejar un mayor volumen de solicitudes.
- **Tolerancia a fallos**: Ayuda a mitigar el impacto de posibles fallos en unos o varios microsersvicios.
- **Alta disponibilidad**: Si un microservicio experimenta una falla o se vuelve inaccesible, el balanceo de carga puede redirigir las solicitudes a otras instancias disponibles. Esto mejora la disponibilidad del sistema en general, ya que los usuarios pueden seguir utilizando los servicios incluso si uno de ellos esta experimentando problemas.
- **Optimizacion de recursos**: El balanceo de carga permite aprovechar al maximo los recursos disponibles en la infraestructura. Distribuye las solicitudes de manera equtativa, evitando sobrecargo de alguna instancia.


# Load balancing con SpringCloud Load Balancer

SCLBalancer es un componente de la plataorma Spring Cloud que oferce capacidades de balanceo de carga para aplicaciones que funcionan en una aquitectura de microservicios.

Su funcion es distribuir de manera equitativa y eficiente las solicitudes entrantes entre multiples instancias de un servicio en funcionamiento para mejorar la disponibilidad, la escalabilidad y el rendimiento del sistema.

## Caracteristicas

- **Balanceo de carga dinamico**: perimte el balanceo de carga dinamico, lo que significa que puede adaptarse automaticamente a la adicion o eliminacion de instancias de servicios en tiempo real.
- I**ntegracion con discovery services**: SCLBalancer se integra con sistemas de descubrimiento de servicios como Eureka o Consul. Puede obtener la lista de instancias disponibles de un servicio registrado en el servidor de descubrimiento y distribuir las solicitudes entre ellas.
- **Algoritmos de balanceo personalizables**: Proporciona la flexibilidad de elegir algoritmos de balanceo personalizados para distribuir las solicitudes. Podes optar por algoritmos como Round Robin, Wighted Round Robin, y mas, segun tus necesidades especificas.
- **Integracion con Spring Cloud Gateway**: SCLBalancer se integra de manera nativa con Spring Cloud Gateway, lo que permite una estrategia de balanceo de carga eficiente para enrutamiento y redireccion de trafico.
- Soporte para el patron Circuit Braker mediante Resilience4J: Puede trabajar en conjunto con circuit brakers o librerias de resiliencia para manejar situaciones en las que un servicio falla o se vuelve inaccesible.
- 