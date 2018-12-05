import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('127.0.0.1', 8889))

client.send("Hello!".encode('utf-8'))

data = client.recv(1024)

print(data.decode('utf-8'))

client.close()
