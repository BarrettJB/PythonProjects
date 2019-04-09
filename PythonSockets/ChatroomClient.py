import socket
import threading
from _thread import *
import time

host = '127.0.0.1'
port = 3656

msg_lock = threading.Lock()

def recvThread(s):
  while(True):
    with msg_lock:
      data = s.recv(1024)
      print(data.decode('utf-8'))
    time.sleep(0.1)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
print("Connected to host")
name = input("Enter username: ")
s.sendall(name.encode('utf-8'))
data = s.recv(1024)
print( data.decode('utf-8'))

start_new_thread(recvThread, (s,))


while(True):
  with msg_lock:
    msg = input(name + ': ')
    s.sendall(msg.encode('utf-8'))