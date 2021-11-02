from common.rmq import get_rmq_conn_and_channel
from producer import producer


if __name__ == '__main__':
    producer.produce_json_to_rmq(*get_rmq_conn_and_channel())
