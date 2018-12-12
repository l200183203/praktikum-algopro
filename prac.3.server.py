#Filename: p_tcpser.py
#TCP Server untuk client p_tcpcli.py
#By@Ainayah Syifa Hendri

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",50005))
s.listen(5)
print "Calculate the area of sphare"
data = ''
while data.lower() != 'quit' :
       komm, addr = s.accept()
       radius = 0
       while data.lower() != 'quit':
              data = komm.recv(1024)
              if data.lower() == 'quit' :
                     s.close()
                     break
              print'Command: ', data
              try:
                     radius = int(data)
                     komm.send('Stored data')
              except ValueError:       
                     if data.lower() == 'calculate':
                            respon = 'the area of sphare with a radius '+str(radius)+' = '+str(4*(22/7)*(radius**2))
                            komm.send(respon)
              
                     else:
                            komm.send('unknown command') 
