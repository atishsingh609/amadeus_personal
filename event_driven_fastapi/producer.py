# producer.py
import pika
import json
from config import RABBITMQ_URL

class RabbitMQProducer:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URL))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue="events")

    def publish_event(self, event_data: dict):
        self.channel.basic_publish(
            exchange="",
            routing_key="events",
            body=json.dumps(event_data)
        )
        print(f"Published: {event_data}")

    def close(self):
        self.connection.close()
