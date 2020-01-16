import socket
import select
import serial

arduinoSerialData = serial.Serial('COM4', 9600)

IP = '192.168.1.30'
PORT = 5566

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, PORT))
s.listen(5)
clientscoket, address = s.accept()
print(f'Connection from {address} has been established!')

while True:
    clientscoket.setblocking(False)
    ready = select.select([clientscoket], [], [], 0.1)
    if ready[0]:
        client_msg = clientscoket.recv(1024)
        client_msg = client_msg.decode('utf-8')
        if client_msg == 'exit':
            clientscoket.send(bytes('exit confirmation', 'utf-8'))
            print('exit message received, closing socket')
            clientscoket.close()
            s.close()
            exit()
        if client_msg == 'None':
            clientscoket.send(bytes('Server: massage is empty, please resend', 'utf-8'))
        else:
            arduinoSerialData.write(bytes(client_msg, 'utf-8'))
            arduinoSerialData.write(bytes('\n', 'utf-8'))
    arduinoIn = ""
    while (arduinoSerialData.inWaiting() > 0):
        arduinoIn = arduinoSerialData.readline().strip().decode("ascii")
        clientscoket.send(bytes("Arduino: " + arduinoIn, 'utf-8'))

    # clientscoket.send(bytes('HartBeat', 'utf-8'))