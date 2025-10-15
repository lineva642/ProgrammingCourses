n = int(input())
consumers = input().split()
p = int(input())

def distribute_partitions(consumers: list, p: int) -> dict:
    res = {consumer: [] for consumer in consumers}

    for pid in range(p):
        cid = pid % len(consumers)
        res[consumers[cid]].append(pid)

    return res

print(distribute_partitions(consumers, p))