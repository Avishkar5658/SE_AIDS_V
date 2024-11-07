import socket
import os

# Server Configuration
UDP_IP = "127.0.0.1"  # Listen on localhost
UDP_PORT = 5005       # Port to listen on

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"Server listening on {UDP_IP}:{UDP_PORT}")

def receive_file(filename):
    with open(filename, 'wb') as f:
        print(f"Receiving file: {filename}")
        while True:
            data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes
            if not data:
                break
            f.write(data)
            print(f"Received {len(data)} bytes from {addr}")

    print(f"File {filename} received successfully.")

# Receive the filename
filename, addr = sock.recvfrom(1024)
filename = filename.decode()
print(f"Receiving {filename} from {addr}")
receive_file(filename)
import socket
import os

# Server Configuration
UDP_IP = "127.0.0.1"  # Listen on localhost
UDP_PORT = 5005       # Port to listen on

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"Server listening on {UDP_IP}:{UDP_PORT}")

def receive_file(filename):
    with open(filename, 'wb') as f:
        print(f"Receiving file: {filename}")
        while True:
            data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes
            if not data:
                break
            f.write(data)
            print(f"Received {len(data)} bytes from {addr}")

    print(f"File {filename} received successfully.")

# Receive the filename
filename, addr = sock.recvfrom(1024)
filename = filename.decode()
print(f"Receiving {filename} from {addr}")
receive_file(filename)