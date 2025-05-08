import streamlit as st
from kafka import KafkaConsumer
import json

st.title("Mensajes en timepo real")

consumer = KafkaConsumer(
    # nombre del topic del cual va a consumir
    'red_social',
    bootstrap_servers = 'localhost:9092',
    auto_offset_reset = 'latest',
    value_deserializer = lambda m: json.loads(m.decode('utf-8'))
)

placeholder = st.empty()

for mensaje in consumer:
    datos = mensaje.value
    with placeholder.container():
        st.markdown(f"{datos['usuario']} dice: {datos['texto']}")