from kafka import KafkaProducer
import json

class KafkaService:
    TOPIC= 'new_character'
    SERVER='localhost:29092' 
    producer = KafkaProducer(bootstrap_servers=SERVER, value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    def sendMessage(message):
        KafkaService.producer.send(KafkaService.TOPIC, message)

        