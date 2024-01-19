import socket
from Api import Message 


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 1234
server_socket.bind((host, port))

server_socket.listen(5) #maximal 5 connections 
print(f"Server listening on {host}:{port}")

while True:
    client_socket, addr = server_socket.accept() #accept blockiert bis client connected, wenn connection da, dann wird ein neues socket objekt zurückgegeben und die client adresse
    print(f"Got connection from {addr}")

    message = "Welcome to the server!" #server sendet welcome message 
    client_socket.send(message.encode('utf-8')) #wird in bytes encoded 

    while True:
        client_message = client_socket.recv(1024).decode('utf-8')
        # if not client_message:
        #     break
        print(f"received message from client: {client_message}")

       
client_socket.close()

