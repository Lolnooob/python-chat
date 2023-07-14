import socket
import threading

clients = []

def handle_client(client_socket):
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        if not message:
            break

        print(message)

        for client in clients:
            if client != client_socket:
                client.send(message.encode('utf-8'))

    clients.remove(client_socket)

    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = 'localhost'
    port = 9999

    server_socket.bind((host, port))

    server_socket.listen(5)
    print(f"Server is listening on {host}:{port}")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Accepted connection from {address[0]}:{address[1]}")

        clients.append(client_socket)

        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

start_server()
