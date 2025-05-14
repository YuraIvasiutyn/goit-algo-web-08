import pika
from faker import Faker
from models.contact import Contact
from config.connect_db import conn

fake = Faker()
credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue='email_queue')

for _ in range(10):
    contact = Contact(
        full_name=fake.name(),
        email=fake.email()
    ).save()

    # Відправляємо ID у чергу
    channel.basic_publish(
        exchange='',
        routing_key='email_queue',
        body=str(contact.id).encode()
    )
    print(f"[Producer] Contact {contact.full_name} added to queue.")

connection.close()
