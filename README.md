# Introduccion Kafka
La practica consta de crear un topic en Kafka, producir y consumir mensajes a través de este.

Los pre-requisitos de la práctica son:
1. Tener instaldo Java(JDK 17 MSI Installer Oracle, el MSI setea a java en las variables de entorno automaticamente, de lo contrario, con otro instalador, usted configura eso)
2. Instalar Kafka Scala 2.13-Kafka 3.6.0(Se recomienda esta versión ya que está bien documentada y utiliza zookeeper, que para nuestros propositos es adecuado)
3. Instalar Python (instalar la librería kafka-python, se puede instalar la librería de la siguiente manera: pip install kafka-python)

Desarrollo de la práctica:
1. Ubicarse en donde se descomprimió el archivo de kafka (idealmente en C:\kafka\kafka_2.13-3.6.0\)
2. Arrancamos Zookeeper con el siguiente comando(Es importante ejecutar primero zookeeper antes que Kafka)(C:\kafka\kafka_2.13-3.6.0\): .\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
3. En una nueva terminal o CMD inicializar Kafka con el siguiente comando(C:\kafka\kafka_2.13-3.6.0\): .\bin\windows\kafka-server-start.bat .\config\server.properties
4. En una nueva terminal se crea un Kafka TOPIC,  en esta práctica se llamará 'red_social'. Creamos el topic con el siguiente comando(C:\kafka\kafka_2.13-3.6.0\): .\bin\windows\kafka-topics.bat --create --topic red_social --bootstrap-server localhost:9092 --partition 1 replication-factor 1
5. En una nueva terminal, ubiquese en donde haya guardado sus archivos python producer.py y consumer.py (e.j. C:\Desktop\kafka_practica\) y ejecute el archivo producer.py con el siguiente comando: python producer.py
6. En una nueva terminal, ubiquese en donde haya guardado sus archivos python producer.py y consumer.py (e.j. C:\Desktop\kafka_practica\) y ejecute el archivo consumer.py con el siguiente comando: python consumer.py

7. Observará cómo se mandan y reciben mensajes en tiempo real.

8. Si se quiere ejecutar el archivo app.py deberá instalar la librería streamlit (puede instalarla con el siguiente comando: pip install streamlit)
9. En una nueva terminal, ubiquese en donde haya guardado sus archivo app.py (e.j. C:\Desktop\kafka_practica\) y ejecute el archivo app.py con el siguiente comando: python app.py, si no funciona trate con este comando: python -m streamlit app.py
