import socket
import threading

def receive_messages(client_socket):
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        if not message:
            break

        print(message)

    client_socket.close()

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_host = 'localhost'
    server_port = 9999

    client_socket.connect((server_host, server_port))
    print(f"Hosted @ {server_host}:{server_port}")

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        message = input()
        if message.lower() == 'quit':
            break
        client_socket.send(message.encode('utf-8'))

    client_socket.close()

start_client()
