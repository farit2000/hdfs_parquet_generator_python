import json

from hdfs import write_parquet_file
from parquet import get_parquet_from_json

MAX_PARQUET_FILE_ROWS = 5000

row_counter = 0
list_of_data = []
file_num = 0


def consumer_callback(ch, method, properties, body):
    global row_counter
    global file_num
    global list_of_data
    if len(list_of_data) <= MAX_PARQUET_FILE_ROWS:
        list_of_data.append(json.loads(body))
    else:
        write_parquet_file(get_parquet_from_json(list_of_data), file_num=file_num)
        list_of_data.clear()
        row_counter = 0
        file_num += 1

    print(" [x] Received %r" % body)


def consume(rmq_conn, rmq_channel):
    try:
        rmq_channel.basic_consume(queue='test', on_message_callback=consumer_callback, auto_ack=True)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        rmq_channel.start_consuming()
    except KeyboardInterrupt:
        print('Interrupted')
        rmq_conn.close()
