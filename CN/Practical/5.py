#Server Code

import socket
import os

# Server details
SERVER_HOST = '192.168.137.1'  # Listen on all interfaces
SERVER_PORT = 5001
BUFFER_SIZE = 4096  # Buffer size for file transfer

# Function to receive a file
def receive_file(connection, filename):
    with open(filename, 'wb') as f:
        print("Receiving file...")
        while True:
            data = connection.recv(BUFFER_SIZE)
            if not data:
                break
            f.write(data)
        print("File received successfully.")

# Create the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(5)

print(f"[*] Listening on {SERVER_HOST}:{SERVER_PORT}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"[+] {client_address} connected.")

    # Part A: Say "Hello" to Each Other
    client_socket.send(b"Hello, Client!")
    message = client_socket.recv(BUFFER_SIZE).decode()
    print(f"Client says: {message}")

    # Part B: File Transfer
    filename = "received_file.txt"
    receive_file(client_socket, filename)

    client_socket.close()
    print(f"[-] {client_address} disconnected.")






# #Client Code


import socket
import os

# Server details
SERVER_HOST = '127.0.0.1'  # Change to server IP if different
SERVER_PORT = 5001
BUFFER_SIZE = 4096  # Buffer size for file transfer

# Function to send a file
def send_file(connection, filename):
    with open(filename, 'rb') as f:
        print("Sending file...")
        while True:
            data = f.read(BUFFER_SIZE)
            if not data:
                break
            connection.sendall(data)
        print("File sent successfully.")

# Create the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((SERVER_HOST, SERVER_PORT))
print(f"[+] Connected to {SERVER_HOST}:{SERVER_PORT}")

# Part A: Say "Hello" to Each Other
message = client_socket.recv(BUFFER_SIZE).decode()
print(f"Server says: {message}")
client_socket.send(b"Hello, Server!")

# Part B: File Transfer
filename = "sample_file.txt"  # Change to the actual file path
if os.path.exists(filename):
    send_file(client_socket, filename)
else:
    print(f"File '{filename}' not found!")

client_socket.close()
