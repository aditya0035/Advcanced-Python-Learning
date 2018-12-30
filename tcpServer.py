import  socket
def Server():
    host="127.0.0.1"
    port=5000
    sock=socket.socket()
    sock.bind((host,port))
    sock.listen(1)
    client, address = sock.accept()
    while True:
        print(f'Communication from {address}')
        data=client.recv(1024).decode("utf-8")
        if not data:
            break;
        print(f"from Connected User{data}")
        data=data.upper()
        print(f"Sending:{data}")
        client.send(data.encode("utf-8"))
    client.close()

if __name__ == '__main__':
    Server()
