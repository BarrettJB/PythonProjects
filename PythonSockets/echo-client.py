import socket

#HOST = '127.0.0.1'
HOST = '98.26.116.113'
PORT = 3656

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print("Connected to host ('exit' to leave)")
shouldContinue = True
while(shouldContinue):
  msg = input()
  s.sendall(msg.encode('utf-8'))
  data = s.recv(1024)
  print('Recived: ', repr(data))
s.close()
