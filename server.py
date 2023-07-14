import socket
import threading

clients = []

def handle_client(client_socket):
    while True:
        # Receive message from client
        message = client_socket.recv(1024).decode('utf-8')
        if not message:
            break

        # Print the received message
        print(message)

        # Send the message to all connected clients
        for client in clients:
            if client != client_socket:
                client.send(message.encode('utf-8'))

    # Remove the client from the list
    clients.remove(client_socket)

    # Close the client connection
    client_socket.close()

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define the host and port to bind the server socket
    host = 'localhost'
    port = 9999

    # Bind the server socket to the host and port
    server_socket.bind((host, port))

    # Start listening for client connections
    server_socket.listen(5)
    print(f"Server is listening on {host}:{port}")

    while True:
        # Accept client connections
        client_socket, address = server_socket.accept()
        print(f"Accepted connection from {address[0]}:{address[1]}")

        # Add the client socket to the list
        clients.append(client_socket)

        # Create a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

start_server()
