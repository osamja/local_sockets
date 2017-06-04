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

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

class App:
    def __init__(self, master):
        self.ip_addr = ip_addr
        self.port = 8080
        self.url = str(self.ip_addr) + ':' + str(self.port)
        self.filenames = []
        self.frame = Frame(master)
        self.frame.pack(fill=X, padx=50, pady=50)
        self.url_label = Label(self.frame, text="%s" % self.url).pack()
        self.upload = Button(master, text="Upload file", command=self.fileupload).pack()  
        self.hi_there = Button(self.frame, text="Hello", command=self.say_hi)
        self.hi_there.pack()
        self.servedFilename = Label(self.frame, text="")
        self.servedFilename.pack()

    def say_hi(self):
        print("hi! self upload: ", self.filenames)

    def showUploadedFile(self):
        self.servedFilename.configure(text="%s" % self.filenames)

    def serveFile(self, path):
        HOST_NAME, PORT_NUMBER = self.ip_addr, self.port
        httpd = thread.start_new_thread(ThreadedHTTPServer((HOST_NAME, PORT_NUMBER), MyHandler))
        print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
        httpd.server_close()
        print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)

    def fileupload(self):   # GET MORE STABLE SOLUTION
        while True:
            uploadedfilenames = askopenfilenames(multiple=True)
            if uploadedfilenames == '':
                tkMessageBox.showinfo(message="File Upload has been cancelled program will stop")
                return
            uploadedfiles = root.tk.splitlist(uploadedfilenames)
            if len(uploadedfiles)!=1:
               tkMessageBox.showinfo(message="Select at least one file!")
               return
            else:
                if uploadedfiles not in self.filenames:
                    self.filenames.append(uploadedfiles)
                #self.serveFile(self.filenames[0][0])
                self.showUploadedFile()
                global path
                path = uploadedfiles[0]
                self.serveFile(path)
                return



path = None     # path to requested uploaded file
fname_nopath = None     # trims path name up to filename
# get ip address
ip_addr = get_ip_addr()
root = Tk()
app = App(root)
root.mainloop()


#root.destroy() # optional; destroys python process if not already done so
