Python 3.9.0 (v3.9.0:9cf6752276, Oct  5 2020, 11:29:23) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> value=0.001
>>> hold=0
>>> inf=[]
import os
from http.server import HTTPServer, CGIHTTPRequestHandler
os.chdir('.')
server_object = HTTPServer(server_address=('', 80), RequestHandlerClass=CGIHTTPRequestHandler)
server_object.serve_forever()
>>> while 1==1:
	inf=['0.00', hold]

	
wallet=0
def buy(x):
if wallet > 0:
print('all out...')
print('adding $100...')
wallet += 100
else:
hold += x
wallet -= x * value

def sell(x):
if hold > x:
print('no more...')
else:
hold -= x
wallet += x*value
