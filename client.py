from threading import Thread
import socket

IP = '192.168.1.30'
PORT = 5566

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))
print(f'connected to server\nIP: {IP}\nPORT: {PORT} ')


def send():
    while True:
        to_send = input()
        if to_send == '':
            to_send = 'None'
        s.send(bytes(to_send, 'utf-8'))
        if to_send == 'exit':
            print('closing socket')
            s.close()
            exit()


def rec():
    while True:
        try:
            msg = s.recv(1024)
            msg = msg.decode('utf-8')
            print(msg)
        except Exception:
            pass


if __name__ == "__main__":
    t1 = Thread(target=send)
    t2 = Thread(target=rec)
    t1.setDaemon(True)
    t2.setDaemon(True)
    t1.start()
    t2.start()
    while True:
        pass
