Goal

Build a real-time event streaming system where an application sends orders, Kafka processes them, and AWS services store and monitor the data.

Architecture

User → Producer App → Kafka → Consumer → AWS Database

Components:

AWS EC2 → host Kafka broker

Kafka Producer → send events (orders)

Kafka Topic → stream messages

Kafka Consumer → process events

AWS RDS / DynamoDB → store processed data

CloudWatch → monitoring

Tools Used

AWS EC2

Apache Kafka

Python

Docker (optional)

AWS RDS or DynamoDB

CloudWatch
