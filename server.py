
import socket
import time

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("0.0.0.0", 12345))

print("====================================")
print(" UDP Clock Sync Server Started")
print(" Listening on port 12345...")
print("====================================")

while True:
    data, addr = server_socket.recvfrom(1024)

    t2 = time.time()   # use SAME clock

    time.sleep(0.005)  # 5 ms delay

    t3 = time.time()   # use SAME clock

    message = f"{t2},{t3}"
    server_socket.sendto(message.encode(), addr)

    print(f"Request from {addr}")
    print(f"t2: {t2}, t3: {t3}\n")