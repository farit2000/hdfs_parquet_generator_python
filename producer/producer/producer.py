import json
import time

from faker import Faker

faker = Faker()


def generate_random_json():
    return json.dumps(
        {
            "uuid": str(faker.uuid4()),
            "first_name": faker.first_name(),
            "last_name": faker.last_name(),
            "birthday": str(faker.date_of_birth()),
            "job": faker.job(),
            "phone_number": faker.phone_number(),
            "address": faker.address()
        }
    )


def produce_json_to_rmq(rmq_conn, rmq_channel):
    try:
        while True:
            rmq_channel.basic_publish(
                exchange='', routing_key='test',
                body=generate_random_json()
            )
            time.sleep(0.01)
            print(" [x] Sent!")
    except KeyboardInterrupt:
        print("Press Ctrl-C to terminate while statement")
        rmq_conn.close()
