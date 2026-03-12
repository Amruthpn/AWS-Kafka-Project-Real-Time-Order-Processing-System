# Solace → Kafka Streaming Pipeline

This project demonstrates real-time event streaming using:

- Solace PubSub+
- Apache Kafka
- Python Integration Service
- Flask Dashboard
- Kafdrop Monitoring
- Docker
- AWS EC2

## Architecture

Event Producer  
→ Solace Broker  
→ Python Integration Service  
→ Kafka Broker  
→ Kafka Consumer  
→ Flask Dashboard  

## Components

Solace Broker (Docker)
Kafka Broker (AWS EC2)
Python Bridge Service
Flask Dashboard
Kafdrop Monitoring UI

## Technologies

Python  
Solace PubSub+  
Apache Kafka  
Docker  
AWS EC2  
Flask  

## Features

- Event-driven architecture
- Real-time message streaming
- Solace to Kafka integration
- Kafka topic monitoring using Kafdrop
- Live dashboard using Flask

## Running the Project

Start Solace:

docker run -d --name solace -p 8080:8080 -p 55555:55555 -p 8008:8008 -e username_admin_globalaccesslevel=admin -e username_admin_password=admin --shm-size=1g solace/solace-pubsub-standard

Start Kafka:

bin/zookeeper-server-start.sh config/zookeeper.properties  
bin/kafka-server-start.sh config/server.properties

Run bridge:

python solace_kafka_bridge.py

Run dashboard:

python app.py
