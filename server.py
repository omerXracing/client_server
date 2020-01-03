import socket
import serial

IP = '192.168.1.30'
PORT = 5566

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, PORT))
s.listen(5)
clientscoket, address = s.accept()
print(f"Connection from {address} has been established!")

while True:
    msg = clientscoket.recv(1024)
    msg = msg.decode("utf-8")
    if msg == "exit":
        print("exit message received, closing socket")
        clientscoket.close()
        s.close()
        break
    else:
        print(msg)
