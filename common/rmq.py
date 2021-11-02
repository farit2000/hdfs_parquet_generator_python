import pika
from pika import PlainCredentials


def get_rmq_conn_and_channel():
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='84.252.132.150',
        credentials=PlainCredentials(
            username='admin',
            password="password"
        )
    ))
    channel = connection.channel()
    channel.queue_declare(queue='test')
    return connection, channel
