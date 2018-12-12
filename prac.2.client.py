# Filename: p_tcpcli.py
# Client TCP untuk server p_tcpser.py
#By @Ainayah Syifa Hendri
import socket

hostname = 'localhost'
message = ''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50004))
print "The communication program about the server"
while message.lower() != 'quit' :
    message = raw_input("Command: ")
    s.send(message)
    if message.lower() != 'quit':
        response = s.recv(1024)
        print 'Output: ', response
s.close()
