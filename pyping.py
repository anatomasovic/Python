# Working on localhost only

import socket
import time

print ("Number of pings:")
n = int(input())
#ICMP_HEADER = b'x08\x00\xF7x00\x00\x00\x00'
ipadd = socket.gethostbyname('www.google.com')
sender = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.getprotobyname("icmp"))
sender.setsockopt(socket.SOL_IP, socket.IP_TTL, 1)
receiver = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.getprotobyname("icmp"))
for i in range (1, n+1):
    start = time.time()
    sender.sendto(bytes('a', 'utf8'), ("www.google.com", 0))
    reply = receiver.recv(1024)
    t = time.time() - start
    print('Request', i, ', Time taken:', t*1000, 'ms')
