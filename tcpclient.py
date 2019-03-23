import socket

TCP_IP = '192.168.0.105'
TCP_PORT = 2014
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
data = s.recv(BUFFER_SIZE)
s.close()

print (data)
