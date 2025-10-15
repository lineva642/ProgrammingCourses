# We need to install and import the Kafka library for our Python application to communicate with Kafka
import json
import uuid

from confluent_kafka import Producer

# we're creating new Kafka producer configuration; we're telling it where Kafka is accessible
# 'localhost:9092' -- KAFKA_ADVERTISED_LISTENERS, where a producer can talk to Kafka server
# 'bootstrap.servers' -- provides the initial hosts that act as the starting point
# for a Kafka client to discover the full set of alive servers in the cluster

producer_config = {
    'bootstrap.servers': 'localhost:9092'
}

producer = Producer(producer_config)

def delivery_report(err, msg):
    if err:
        print(f"❌ Delivery failed: {err}")
    else:
        # we convert message back from bytes to characters
        print(f"✅ Delivered: {msg.value().decode("utf-8")}")
        print(f"✅ Delivered to {msg.topic()}: partition {msg.partition()}: at offset {msg.offset()}")
        # ✅ Delivered to orders: partition 0: at offset 3
        # offset = 3 as it was the 3rd message that we sent to Kafka
        # dir() -- returns a list of all attributes and methods available for an object
        # print(dir(msg))

# create an event that will be sent to Kafka
order = {
    "order_id": str(uuid.uuid4()),
    "user": "vika",
    "item": "mushroom pizza",
    "quantity": 2
}

order_2 = {
    "order_id": str(uuid.uuid4()),
    "user": "liza",
    "item": "shawarma",
    "quantity": 1
}


# we created an event in JSON format
# now we need to convert it to Kafka compatible format, which is bytes

# it will turn dict to str and then encode this string into byte format, which Kafka understands
# value = json.dumps(order).encode('utf-8')
value = json.dumps(order_2).encode('utf-8')

# if topic doesn't exist in Kafka yet, it will be created automatically
# we can add additional functionality to track whether a send message was delivered to Kafka or not
# to do this we will add callback -- a function that takes err or msg as inputs and make smth based on them
producer.produce(
    topic='orders',
    value=value,
    callback=delivery_report
)

# A producer actually doesn't send events one by one in Kafka.
# It buffers them and then sends by batch
# If the producer crashes at some point,
# the flush will make sure all these buffered unsent events get sent before exiting the program
producer.flush()
