import socket
from _thread import *
import threading

print_lock = threading.Lock()
conns = []

#Thread function
def threaded(c,username):
  global conns
  while True:
    #Get data from client
    data = c.recv(1024)
    # if not data:
    #   with print_lock:
    #     print('Bye!')
    #     break

    # #Reverse the data string and send it back
    # data = data[::-1]
    # c.send(data)
    msg = username + ': ' + data.decode('utf-8')
    #Send the data to all other connections
    for conn in conns:
      if conn != c:
        conn.send(msg.encode('utf-8'))

  #On exit close the connection
  c.close()
  conns.remove(c)

def Main():
  global conns
  host = ""
  port = 3656
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.bind((host,port))
  print("Socket bound to port", port)

  #Set the socket to listen
  s.listen(5)
  print("Socket is listening")

  #loop until the client exits
  while True:
    c, addr = s.accept()
    conns.append(c)
    print('Connected to :', addr[0], ':', addr[1])
    username = c.recv(1024)
    msg = 'Hello ' + username.decode('utf-8')
    c.send(msg.encode('utf-8'))
    #Start a new thread to handle
    start_new_thread(threaded, (c,username.decode('utf-8'),))

  s.close()

if __name__ == '__main__':
  Main()