import pika
from elasticsearch import Elasticsearch
from datetime import datetime
import os


RABBITMQ_QUEUE_NAME = os.environ['RABBITMQ_QUEUE_NAME']
RABBITMQ_USERNAME = os.environ['RABBITMQ_USERNAME']
RABBITMQ_PASSWORD = os.environ['RABBITMQ_PASSWORD']
ES_USERNAME = os.environ['ES_USERNAME']
ES_PASSWORD = os.environ['ES_PASSWORD']

print("[INFO] Connecting to Elasticsearch...")
es = Elasticsearch(['http://elasticsearch:9200'], http_auth=(ES_USERNAME, ES_PASSWORD), request_timeout=30)
print("[INFO] Connected to Elasticsearch!")

def callback(ch, method, properties, body):
    print(f" [x] Received message from RabbitMQ: {body.decode('utf-8')}")
    doc = {
        'message': body.decode('utf-8'),
        'timestamp': datetime.utcnow(),
    }
    response = es.index(index=RABBITMQ_QUEUE_NAME, body=doc)
    print(f" [INFO] Message indexed in Elasticsearch with ID: {response['_id']}")

print("[INFO] Connecting to RabbitMQ...")
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='rabbitmq', 
    credentials=pika.PlainCredentials(RABBITMQ_USERNAME, RABBITMQ_PASSWORD),
    socket_timeout=20,
    connection_attempts=3
))
print("[INFO] Connected to RabbitMQ!")

print("[INFO] Connecting to channel RabbitMQ...")
channel = connection.channel()
print("[INFO] Connected to channel RabbitMQ!")

channel.queue_declare(queue=RABBITMQ_QUEUE_NAME, durable=True)
print(f" [*] Waiting for messages in {RABBITMQ_QUEUE_NAME}. To exit press CTRL+C")

channel.basic_consume(queue=RABBITMQ_QUEUE_NAME, on_message_callback=callback, auto_ack=True)
channel.start_consuming()
