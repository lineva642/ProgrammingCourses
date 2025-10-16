# from confluent_kafka.admin import AdminClient, NewTopic
# from confluent_kafka import Producer, Consumer, TopicPartition
#
#
# admin_client = AdminClient({'bootstrap.servers': 'localhost:9092'})
#
# p = int(input()) # number of partitions
# n = int(input()) # number of messages
#
# topic_name = 'test'
# new_topic = NewTopic(topic_name, num_partitions=p, replication_factor=1)
#
# # # create a new topic with specified number of partitions
# admin_client.create_topics([new_topic])
#
# # we sent messages to Kafka in round-robin mode
# # def delivery_report(err, msg):
# #     if err:
# #         print("Delivery failed:", err)
# #     else:
# #         print(f"Produced '{msg.value().decode()}' to partition {msg.partition()} (offset {msg.offset()})")
#
# producer = Producer({'bootstrap.servers': 'localhost:9092'})
# for i in range(n):
#     msg = input()
#     partition = i % p
#     producer.produce(topic_name, msg.encode('utf-8'), partition=partition)
#     producer.flush()
#
# # producer.flush()
#
# # # now we need to read messages in each partition
# consumer_config = {
#     'bootstrap.servers': 'localhost:9092',
#     'group.id': 'order-tracker',
#     'auto.offset.reset': 'earliest'
# }
# consumer = Consumer(consumer_config)
#
# metadata = consumer.list_topics(topic_name)
#
# partitions = [p.id for p in metadata.topics[topic_name].partitions.values()]
#
# for pid in partitions:
#     consumer.assign([TopicPartition(topic_name, pid, 0)])
#
#     pid_msg = []
#     while True:
#         msg = consumer.poll(1.0)
#
#         if msg is None:
#             break
#         if msg.error():
#             continue
#
#         pid_msg.append(msg.value().decode('utf-8'))
#
#     print(' '.join(pid_msg))
#
# consumer.close()
from collections import defaultdict

p = int(input()) # number of partitions
n = int(input()) # number of messages

partitions = defaultdict(list)

for i in range(n):
    pid = i % p
    text = input()
    partitions[pid].append(text)

for pid, msgs in partitions.items():
    print(*msgs)




