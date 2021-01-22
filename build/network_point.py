import miner
import time
localtime = time.asctime( time.localtime(time.time()) )
thetime=localtime
miner.initialize()
print('started at:'thetime)
import os
from http.server import HTTPServer, CGIHTTPRequestHandler
os.chdir('.')
server_object = HTTPServer(server_address=('', 80), RequestHandlerClass=CGIHTTPRequestHandler)
print('connected to server')
server_object.serve_forever()
while 1==1:
    
    time.sleep(300)
    print(PHO[-1])
