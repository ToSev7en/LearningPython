import socket
from urllib.parse import urlparse

def get_url(url):
    # request html by socket
    url = urlparse(url)
    host = url.netloc
    path = url.path

    if path == "":
        path = "/"

    # 建立 socket 连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect((host, 80)) # ip or domain_name

    client.send("GET {} HTTP/1.1\r\n\r\nHost:{}\r\nConnection:close".format(path, host).encode('utf-8'))

    data = b""

    while True:
        d = client.recv(1024)
        if d:
            data += d
        else:
            break
    data = data.decode('utf-8')

    html_data = data.split('\r\n\r\n')[1]

    print(html_data)

    client.close()



if __name__ == "__main__":
    get_url("http://www.baidu.com")
