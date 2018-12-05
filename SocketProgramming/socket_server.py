import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 不能写成 127.0.0.1 ，在本机局域网 ip 访问不到
server.bind(('0.0.0.0', 8889))

server.listen()

sock, addr = server.accept()

# 获取从 Client 发来到数据, 一次获取 1k 大小的数据
data = sock.recv(1024)
print(data.decode('utf-8'))

sock.send("Hi! This is TSW!".encode('utf-8'))

server.close()
sock.close()