import socket

host = '127.0.0.1'
port = 9000 

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

print("Waiting ...")

client_socket, client_address = server_socket.accept()
print("--------------- Client connected ---------------")

while True:
    encrypted_message = client_socket.recv(1024).decode()
    print("Received message from client:", encrypted_message)

    if encrypted_message == "bye":
        break

    response = input("Enter your response: ")
    client_socket.send(response.encode())

client_socket.close()
server_socket.close()