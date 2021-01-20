import miner
import time
localtime = time.asctime( time.localtime(time.time()) )
thetime=localtime
miner.initialize()
print('started at:'thetime)
while 1==1:
    print(PHO[-1])
import os
from http.server import HTTPServer, CGIHTTPRequestHandler
os.chdir('.')
server_object = HTTPServer(server_address=('', 80), RequestHandlerClass=CGIHTTPRequestHandler)
server_object.serve_forever()

