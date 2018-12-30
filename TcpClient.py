import socket

def client():
    host="127.0.0.1"
    port=5000
    sock=socket.socket()
    sock.connect((host,port))
    msg=input("->")
    while msg!='q':
        sock.send(msg.encode("utf-8"))
        data=sock.recv(1024).decode("utf-8")
        print(f"recv from server:{data}")
        msg=input("->")
    sock.close()

if __name__ == '__main__':
    client()
