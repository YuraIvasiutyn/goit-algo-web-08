import pika
from bson import ObjectId
from models.contact import Contact
from config.connect_db import conn


def send_email_stub(contact):
    print(f"[Consumer] Sending email to {contact.email} (stub)")


def callback(ch, method, properties, body):
    contact_id = body.decode()
    contact = Contact.objects(id=ObjectId(contact_id)).first()
    if contact and not contact.sent:
        send_email_stub(contact)
        contact.sent = True
        contact.save()
        print(f"[Consumer] Email sent to {contact.full_name}")


credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue='email_queue')

channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=True)

print('[*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
