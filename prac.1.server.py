#Filename: p_tcpser.py
#TCP Server untuk client p_tcpcli.py
# By @Ainayah Syifa Hendri
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",50007))
s.listen(5)
print "The auto answering server's ready"
data = ''
dictionary = {'Name' : 'Ainayah Syifa Hendri',
              'NIM' : 'L200183203',
              'Generation' : '2018'}
while data.lower() != 'exit' :
       komm, addr = s.accept()
       while data.lower() != 'exit':
              data = komm.recv(1024)
              if data.lower() == 'exit' :
                     komm.send('ready!!')
                     s.close()
                     break
              print'Question: ', data
              if dictionary.has_key(data):
                     komm.send(dictionary[data])
              else:
                     komm.send('Your question is irrelevant') 
