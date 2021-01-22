req=[]
con=0
tic=0
made=0
import os
import random as r
from http.server import HTTPServer, CGIHTTPRequestHandler
os.chdir('smart_contract')
# dont ever change 'smart_contract' to anything else
server_object = HTTPServer(server_address=('contract', 80), RequestHandlerClass=CGIHTTPRequestHandler)
# change 'contract' to your contract name
while True:
    con = r.randint(0, 1)
    req.append(transID)
    req.append(con)

def setup_contract_adress(X):
    adress=r.randint(1111, 9999) + '.' + X
    print('=================New adress: ' + adress + '=================')
    # 'X' should be the length of the name of your contract (ex: "CONTRACT" would be 8)

def find_requests(Y):
    while Y != 0:
        retrn.append(req[tic])
        tic += 1
        Y -= 1
        return retrn
    # 'Y' should be how many requsets you want to fulfill

def fulfil_requests():
    tic=0
    ln = len(retrn)
    while ln != 0:
        if retrn[tic] == 1:
            made+=0.0254
    ln -= 1
    tic += 1
    retrn.pop(ln)
    
def setup_full_contract():
    setup_contract_adress()
    find_requests(Y)
    fulfill_requests()
    import valuex
    value +=1
    




# these define all the functions you will need to build your contract

server_object.serve_forever('contract')
# change 'contract' to your contract name
