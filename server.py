import socket
s=socket.socket()
print("Socket has created succesffuly")
port=56789
s.bind(("",port))
print(f"Socket binded to port {port}")
s.listen(5)
print("Socket is listening")
while True:
    c, addr = s.accept()
    print("Got connection from ", addr)
    messasge="Thnak you for connection"
    c.send(messasge.encode())
    c.close()
    