import socket

host = '127.0.0.1'
port = 9000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

while True:
    message = input("Enter a message: ")
    client_socket.send(message.encode())

    if message == "bye":
        break

    response = client_socket.recv(1024).decode()
    print("Received response from server:", response)

client_socket.close()
