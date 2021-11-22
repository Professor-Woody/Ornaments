import usocket as socket

import network
import esp
esp.osdebug(None)

import gc
gc.collect()

from Model import *

class Controller:
    def __init__(self):
        # setup wifi
        ssid = 'OrnamentNet'
        password = 'ornaments'

        ap = network.WLAN(network.AP_IF)
        if not ap.active():
            ap.active(True)
        print ("Access point: {}".format(ap.ifconfig()))


        # setup listener socket
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(('', 80))
        self.s.listen(5)

        # setup model
        self.model = Model()
        self.keepGoing = True

        # setup routes
        self.routes = {
            'GET':
            {    
                '/': self.model.homepage,
                '/test': self.model.test,
                '/getProgram': self.model.getProgram,
            },
            'POST':
            {}
        }


    def run(self):
        while self.keepGoing:
            # get connection
            conn, addr = self.s.accept()
            print ("got connection from {}".format(addr))
            request = conn.recv(1024)
            print(request)
            request = request.decode()
            print ("")

            requestType, route, args = self.parseRequest(request)
            response = self.handleRequest(requestType, route, args)
            self.sendResponse(conn, response)



    # =============================
    def parseRequest(self, request):
        request = request.split()

        requestType = request[0]

        args = {}
        if '?' in request[1]:
            route, arguments = request[1].split('?')
            arguments = arguments.split('&')
            for arg in arguments:
                arg = arg.split('=')
                args[arg[0]] = arg[1]
        else:
            route = request[1]
        

        print ("==========\nRequest Type: {}\nRoute: {}\nArgs: {}".format(requestType, route, args))
        return requestType, route, args

    # ==============================
    def handleRequest(self, requestType, route, args):
        if requestType in self.routes.keys():
            if route in self.routes[requestType].keys():
                return self.routes[requestType][route](args)
            return "bad request 1"
        return "bad request 2"
        

    # ==============================
    def sendResponse(self, conn, response):
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()

c = Controller()
