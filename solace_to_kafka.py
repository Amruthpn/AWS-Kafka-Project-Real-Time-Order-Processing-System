from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers="54.201.215.233:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

while True:
    message = {
        "source": "solace",
        "event": "order",
        "timestamp": time.time()
    }

    producer.send("solace-kafka", message)
    print("Forwarded to Kafka:", message)

    time.sleep(3)
