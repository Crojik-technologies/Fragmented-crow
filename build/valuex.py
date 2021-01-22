value=0.01
import masternode
import os
from http.server import HTTPServer, CGIHTTPRequestHandler
os.chdir('valuer')
server_object = HTTPServer(server_address=('values', 80), RequestHandlerClass=CGIHTTPRequestHandler)
server_object.serve_forever(value)
