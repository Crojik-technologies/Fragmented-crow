import miner
import random
ID=[]
ip=0
def setupNOD(ip):
    ip=random.randint(1111, 9999)
    ID=['NOD', '.', ip]
    import os
from http.server import HTTPServer, CGIHTTPRequestHandler
os.chdir('.')
server_object = HTTPServer(server_address=('', 80), RequestHandlerClass=CGIHTTPRequestHandler)
server_object.serve_forever()

def setupGHO(ip):
    ip=random.randint(1111, 9999)
    ID=['GHO', '.', ip]
    import os
from http.server import HTTPServer, CGIHTTPRequestHandler
os.chdir('.')
server_object = HTTPServer(server_address=('', 80), RequestHandlerClass=CGIHTTPRequestHandler)
server_object.serve_forever()


def setupEGH(ip):
    ip=random.randint(1111, 9999)
    ID=['EGH', '.', ip]
    import os
from http.server import HTTPServer, CGIHTTPRequestHandler
os.chdir('.')
server_object = HTTPServer(server_address=('', 80), RequestHandlerClass=CGIHTTPRequestHandler)
server_object.serve_forever()


def setupKIplus(ip):
    ip=random.randint(1111, 9999)
    ID=['KI+', '.', ip]
    import os
from http.server import HTTPServer, CGIHTTPRequestHandler
os.chdir('.')
server_object = HTTPServer(server_address=('', 80), RequestHandlerClass=CGIHTTPRequestHandler)
server_object.serve_forever()


def setupGminus(ip):
    ip=random.randint(1111, 9999)
    ID=['N/A', '.', ip]
    import os
from http.server import HTTPServer, CGIHTTPRequestHandler
os.chdir('.')
server_object = HTTPServer(server_address=('', 80), RequestHandlerClass=CGIHTTPRequestHandler)
server_object.serve_forever()

