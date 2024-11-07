import socket
import os

# Server Configuration
UDP_IP = "127.0.0.1"  # Connect to localhost where server is running
UDP_PORT = 5005       # Port of the server

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send_file(filename):
    if not os.path.exists(filename):
        print(f"File {filename} does not exist.")
        return

    # Send the filename first
    sock.sendto(filename.encode(), (UDP_IP, UDP_PORT))

    with open(filename, 'rb') as f:
        print(f"Sending file: {filename}")
        while True:
            data = f.read(1024)  # Read file in chunks of 1024 bytes
            if not data:
                break
            sock.sendto(data, (UDP_IP, UDP_PORT))
            print(f"Sent {len(data)} bytes")

    print(f"File {filename} sent successfully.")

def read_file(filename):
    if not os.path.exists(filename):
        print(f"File {filename} does not exist.")
        return

    try:
            with open(filename, 'r', encoding='utf-8') as f:
             content = f.read()
            print(f"Contents of {filename}:\n")
            print(content)
    except UnicodeDecodeError:
        print(f"File {filename} is not a text file or contains non-UTF-8 characters.")
        print("Reading in binary mode:")
        with open(filename, 'rb') as f:
            content = f.read()
            print(f"Binary contents of {filename}:\n")
            print(content)


# Main program loop
if __name__ == "__main__":
    operation = input("Enter 's' to send a file or 'r' to read a file locally: ").strip().lower()

    if operation == 's':
        filename = input("Enter the name of the file to send: ").strip()
        send_file(filename)
    elif operation == 'r':
        filename = input("Enter the name of the file to read: ").strip()
        read_file(filename)
    else:
        print("Invalid option. Please enter 's' to send a file or 'r' to read a file.")