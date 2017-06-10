

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn
import threading
from Tkinter import *
import socket
from tkFileDialog import askopenfilenames
import tkFileDialog
import tkMessageBox
import pdb
import sys
from ip import get_ip_addr
import time
import BaseHTTPServer
import thread
from threading import Thread

"""
Isolated testing of the server. 
    - No GUI or fileuploading involved so that server testing is more rapid.  
    - Import classes and functions from main.   
"""

# Server handler
class MyHandler(BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(s):      #"""Respond to a GET request."""
        if (s.path == path):  # retrieve uploaded file
            print("Sending download...")
            s.send_response(200)
            s.send_header("Content-type", "multipart/form-data")
            s.end_headers()
            file = open(path, 'rb')
            l = file.read(1024)
            while(l):
                s.wfile.write(l)
                l = file.read(1024)
            file.close()
            return
        s.send_response(200)            # display HTML pg
        s.send_header("Content-type", "text/html")
        s.end_headers()
        s.wfile.write("Download <a href=")
        s.wfile.write("%s" % path)
        s.wfile.write(">file</a>")


def threadServer():
    global serve_counter
    if (serve_counter == 0):
        t1 = Thread(target=serveFile)
        t1.start()
        return
    serve_counter += 1
    print("Serve counter: ", serve_counter)
    t1.run()

def serveFile():
    if (serve_counter > 0):
        print("Closed previous session")
        httpd.server_close()
    HOST_NAME, PORT_NUMBER = ip_addr, port
    httpd = BaseHTTPServer.HTTPServer((HOST_NAME, PORT_NUMBER), MyHandler)
    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)

serve_counter = 0
path = '/Users/sammy/local_sockets/app/mytext.txt'
ip_addr = '10.0.1.55'
port = 8080
threadServer()
path = '/Users/sammy/local_sockets/app/otherText.txt'
threadServer()

