import socket
import threading

def receive_messages(client_socket):
    while True:
        # Receive message from server
        message = client_socket.recv(1024).decode('utf-8')
        if not message:
            break

        # Print the received message
        print(message)

    # Close the client socket
    client_socket.close()

def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define the server host and port
    server_host = 'localhost'
    server_port = 9999

    # Connect to the server
    client_socket.connect((server_host, server_port))
    print(f"Connected to {server_host}:{server_port}")

    # Create a new thread to receive messages from the server
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    # Send messages to the server
    while True:
        message = input()
        if message.lower() == 'quit':
            break

        # Send the message to the server
        client_socket.send(message.encode('utf-8'))

    # Close the client socket
    client_socket.close()

start_client()
