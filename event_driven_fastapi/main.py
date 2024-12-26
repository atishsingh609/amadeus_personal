# main.py
from fastapi import FastAPI
from producer import RabbitMQProducer
import uuid

app = FastAPI()
producer = RabbitMQProducer()

@app.on_event("shutdown")
def shutdown():
    producer.close()

@app.post("/send-event/")
async def send_event(data: dict):
    event_id = str(uuid.uuid4())
    event_data = {"id": event_id, **data}
    producer.publish_event(event_data)
    return {"status": "Event published", "event_id": event_id}
