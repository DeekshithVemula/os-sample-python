#!/usr/bin/env python
import pika
from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    connection = pika.BlockingConnection(
         pika.ConnectionParameters(host='rabbitmq-cluster'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
    connection.close()
    return "Hello World!"

if __name__ == "__main__":
    application.run()
