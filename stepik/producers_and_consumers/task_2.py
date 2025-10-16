num_partitions = int(input())
consumer_ids = input().split()

def assign_partitions(num_partitions: int, consumer_ids: list[str]):
    res = {_id: [] for _id in consumer_ids}

    for i in range(num_partitions):
        consumer_id = i % len(consumer_ids)
        res[consumer_ids[consumer_id]].append(i)

    return res

print(assign_partitions(num_partitions, consumer_ids))