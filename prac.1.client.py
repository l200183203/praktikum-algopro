# Filename: p_tcpcli.py
# Client TCP untuk server p_tcpser.py
# By @Ainayah Syifa Hendri
import socket

hostname = 'localhost'
message = ''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50007))
print "Automatic answering machine is ready"
while message.lower() != 'exit' :
    message = raw_input("Questions: ")
    s.send(message)
    if message.lower() != 'exit':
        response = s.recv(1024)
        print 'The answer: ', response
response = s.recv(1024)
print 'The answer: ', response
s.close()
