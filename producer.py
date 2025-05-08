# Permite enviar mensajes a Kafka
from kafka import KafkaProducer
import json
import time
import random

# Inicializar el productor, creando un productor Kafka
producer = KafkaProducer(
    # indica dónde está Kafka
    bootstrap_servers = 'localhost:9092',
    # Kafka trabaja con bytes
    # Se convierten los mensajes(dict) en json y despues
    # se codifican en formato UTF-8 a bytes
    value_serializer = lambda v: json.dumps(v).encode('utf-8')
)

# Datos simulados
usuarios = ['Ana', 'Luis', 'Enrique', 'Ricardo']
mensajes = ['¡Hola chicos del tec!', 'Kafka es genial', 'Estoy aprendiendo Kafka', '¿Fácil o difícil?']

while True:
    mensaje = {
        'usuario': random.choice(usuarios),
        'texto': random.choice(mensajes)
    }
    producer.send('red_social', mensaje)
    print("Mensaje enviado:", mensaje)
    time.sleep(1)

