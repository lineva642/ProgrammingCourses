import json

from confluent_kafka import Consumer

consumer_config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'order-tracker', # group.id -- identifies a group of consumers that are actually instances of the same program
                                 # Kafka will distribute load between them automatically, they'll read these events in parallel
    'auto.offset.reset': 'earliest' # It tells Consumer what to do if it can;t find where it last left off reading messages
    # it will start with the oldest message in the topic
}

consumer = Consumer(consumer_config)

consumer.subscribe(["orders"])

print("🟢 Consumer is running and subscribed to orders topic")

try:
    while True:
        msg = consumer.poll(1.0) # the consumer asks Kafka is there any new events in subscribed topics
        if msg is None: # msg = None if there is no new events
            continue

        if msg.error(): # an error in connection or in reading
            print("❌ Error:", msg.error())
            continue

        value = msg.value().decode("utf-8")
        order = json.loads(value) # dict representation on a new event in Kafka
        print(f"📦 Received order: {order['quantity']} * {order['item']} from {order['user']}")
except KeyboardInterrupt:
    print("\n🔴 Stopping consumer")

finally:
    consumer.close()