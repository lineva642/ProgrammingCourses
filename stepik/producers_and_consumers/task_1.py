n_msg = int(input())
msg_sizes = [int(size) for size in input().split()]
batch_size = int(input())
send_times = [int(time) for time in input().split()]
linger_ms = int(input())

def calculate_n_batches(
        msg_sizes: list[int],
        send_times: list[int],
        batch_size: int,
        linger_ms: int
) -> int:
    curr_size = 0
    start_time = None
    n_batches = 0

    for msg_size, msg_time in zip(msg_sizes, send_times):
        if start_time is None or msg_time - start_time > linger_ms or curr_size + msg_size > batch_size:
            n_batches += 1
            start_time = msg_time
            curr_size = msg_size
        else:
            curr_size += msg_size


    return n_batches

print(calculate_n_batches(msg_sizes, send_times, batch_size, linger_ms))
