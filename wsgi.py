#!/usr/bin/env python
import pika
import rabbitmq
from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    credentials = pika.PlainCredentials('test','test')
    parameters = pika.ConnectionParameters('10.128.1.62',5672,'/',credentials)
    connection = pika.BlockingConnection(parameters)
    

    channel = connection.channel()
    channel.queue_declare(queue='hello')

    channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
   
    connection.close()
    return "Hello World Hiiii! connection creatteeed"

if __name__ == "__main__":
    application.run()
