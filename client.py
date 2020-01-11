import socket

IP = '192.168.1.30'
PORT = 5566

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))
print(f'connected to server\nIP: {IP}\nPORT: {PORT} ')

while True:
    toSend = input('Data to send: ')
    if toSend == '':
        toSend = 'None'
    s.send(bytes(toSend, 'utf-8'))
    if toSend == 'exit':
        print('closing socket')
        s.close()
        break
    msg = s.recv(1024)
    msg = msg.decode('utf-8')
    print(msg)
