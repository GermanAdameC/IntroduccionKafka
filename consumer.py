from kafka import KafkaConsumer
import json

# Iniciarlizar el consumidor
consumer = KafkaConsumer(
    # nombre del topic del cual va a consumir
    'red_social',
    bootstrap_servers = 'localhost:9092',
    auto_offset_reset = 'earliest',
    value_deserializer = lambda m: json.loads(m.decode('utf-8'))
)

print("Esperando mensajes....\n")

for mensaje in consumer:
    datos = mensaje.value
    print(f"{datos['usuario']} dijo: {datos['texto']}")