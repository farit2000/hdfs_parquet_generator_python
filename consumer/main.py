from common.rmq import get_rmq_conn_and_channel
from consumer import consumer

if __name__ == '__main__':
    consumer.consume(*get_rmq_conn_and_channel())
