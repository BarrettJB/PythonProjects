import socket

HOST = '127.0.0.1'
#HOST = '98.26.116.113'
PORT = 3656

while True:
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
  s.bind((HOST,PORT))
  print('Listening for connection')
  s.listen()
  conn, addr = s.accept()
  print('Connected by', addr)
  while True:
    data = conn.recv(1024)
    if not data:
      print('Client disconnected...')
      break
    print(data)
    conn.sendall(data)
  conn.close()
  s.close()