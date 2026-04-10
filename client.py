
import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ("127.0.0.1", 12345)

print("====================================")
print(" UDP Clock Sync Client Started")
print("====================================")

offsets = []
delays = []

for i in range(5):
    print(f"\n--- Iteration {i+1} ---")

    t1 = time.time()   # SAME clock
    client_socket.sendto(b"Request", server_address)

    data, _ = client_socket.recvfrom(1024)

    t4 = time.time()   # SAME clock

    t2, t3 = map(float, data.decode().split(","))

    offset = ((t2 - t1) + (t3 - t4)) / 2
    delay = (t4 - t1) - (t3 - t2)

    offsets.append(offset)
    delays.append(delay)

    print(f"t1 (Client Send)    : {t1}")
    print(f"t2 (Server Receive) : {t2}")
    print(f"t3 (Server Send)    : {t3}")
    print(f"t4 (Client Receive) : {t4}")
    print(f"Offset              : {offset}")
    print(f"Delay               : {delay}")

avg_offset = sum(offsets) / len(offsets)
avg_delay = sum(delays) / len(delays)

corrected_time = time.time() + avg_offset

print("\n====================================")
print(" FINAL RESULTS")
print("====================================")
print(f"Average Offset        : {avg_offset}")
print(f"Average Delay        : {avg_delay}")
print(f"Drift Correction : {corrected_time}")