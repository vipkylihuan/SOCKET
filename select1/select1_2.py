
import socket

obj = socket.socket()

obj.connect(('127.0.0.1',8081))

while True:
    inp = input("Please(q\退出):\n>>>")
    obj.sendall(bytes(inp,encoding="utf-8"))
    if inp == "q":
        break
    ret = str(obj.recv(1024),encoding="utf-8")
    print(ret)

