import solace.messaging.messaging_service as messaging_service
from solace.messaging.resources.queue import Queue

service = messaging_service.MessagingService.builder() \
    .from_properties({
        "solace.messaging.transport.host": "localhost:55555",
        "solace.messaging.service.vpn-name": "kafka-test",
        "solace.messaging.authentication.basic.username": "admin",
        "solace.messaging.authentication.basic.password": "admin"
    }).build().connect()

queue = Queue.durable_exclusive_queue("kafka-queue")

receiver = service.create_persistent_message_receiver_builder() \
    .with_queue(queue).build().start()

message = receiver.receive_message()
