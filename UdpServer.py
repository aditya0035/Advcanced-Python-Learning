import socket
def Main():
    host="127.0.0.1"
    port=5002
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind((host,port))
    print(f"Server Started")
    while True:
        #as connection less so we need to data and
        #address from where data came from
        data,address=s.recvfrom(1025)
        data=data.decode("utf-8")
        print(f"Message from:{address}")
        print(f"From Connected User:{data}")
        data=data.upper()
        print(f"Sending Data:{data}")
        s.sendto(data.encode("utf-8"),address)
    s.close()
if __name__ == '__main__':
    Main()
