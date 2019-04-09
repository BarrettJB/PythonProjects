import selectors
import socket

HOST = '127.0.0.1'
PORT = 3656

sel = selectors.DefaultSelector()
lsock