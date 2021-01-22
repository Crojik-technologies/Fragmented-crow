import masternode as mn
import network_point as np
import time
import os
from http.server import HTTPServer, CGIHTTPRequestHandler
os.chdir('.')
server_object = HTTPServer(server_address=('', 80), RequestHandlerClass=CGIHTTPRequestHandler)
m1=0
m2=0
m3=0
m4=0
key=0
idd=[]
blk=idd
PHO=[]
a=1
def initialize(ID):
    a=1
    idd=[m1,'.',m4,'.',inf]
    server_object.serve_forever()
    while a==1:
        m1+=m2
        m2+=m3
        m3+=m4
        m4+=m1
        m1+=1
        print(m1)
        print('_____')
        print(m2)
        print('_____')
        print(m3)
        print('_____')
        print(m4)
        print('_____')
        time.sleep(0.2)
        print('mined block ' + blk)
        ID=idd
        idd.append(blk)
        blk=idd
        PHO.append(blk, m1, m2, m3, ,m4)
        value+=inf

def stop():
    a+=1
    print('                                                                                             ')
    print('stopped')
    value-=inf

while 1==1:
    time.sleep(3600)
    value-=inf
        
