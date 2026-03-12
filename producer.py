from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='54.201.215.233:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    order = {
        "order_id": random.randint(1000,9999),
        "symbol": random.choice(["SOLACE","KAFKA","MIDDLEWARE","JMS"]),
        "price": round(random.uniform(100,500),2)
    }

    producer.send("solace-kafka", order)
    print("Sent:", order)

    time.sleep(1)
