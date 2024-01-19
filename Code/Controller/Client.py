import socket
import requests

host = '127.0.0.1'
port = 1234

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INIT ist die Adressfamilie für IPv4, SOCK_STREAM um daten in der gesendeten Reihenfolge zu senden 
server_adress = (host, port)
client_socket.connect(server_adress) #verbindet server

message = client_socket.recv(5678).decode('utf-8')
print(f"received message from server: {message}") #client erhält message vom server, erhaltene bytes werden zum string mit utf-8

while True:
    user_input = input("Type a message to send it to the server (type 'exit' to quit)")
    if user_input.lower() == exit:
        break
    client_socket.send(user_input.encode('utf-8'))



client_socket.close()