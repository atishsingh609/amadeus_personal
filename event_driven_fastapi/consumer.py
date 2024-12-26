# consumer.py
import pika
import redis
import json
from config import RABBITMQ_URL, REDIS_HOST, REDIS_PORT

class RabbitMQConsumer:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URL))
        self.channel = self.connection.channel()
        self.redis_client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

    def callback(self, ch, method, properties, body):
        event_data = json.loads(body)
        print(f"Received: {event_data}")
        self.process_event(event_data)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def process_event(self, event_data: dict):
        # Example: Store event in Redis
        event_id = event_data.get("id")
        self.redis_client.set(f"event:{event_id}", json.dumps(event_data))
        print(f"Processed and stored event in Redis: {event_data}")

    def start_consuming(self):
        self.channel.queue_declare(queue="events")
        self.channel.basic_consume(queue="events", on_message_callback=self.callback)
        print("Waiting for messages...")
        self.channel.start_consuming()
