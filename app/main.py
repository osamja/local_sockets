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

""" Display landing webpage at IP_ADDR:PORT and allow download of PATH file. """
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
        s.send_response(200)       
        s.send_header("Content-type", "text/html")
        s.end_headers()
        s.wfile.write("Download <a href=")
        s.wfile.write("%s" % path)
        s.wfile.write(">file</a>")

""" The main GUI app. Initializes GUI window and button events. """
class App:
    def __init__(self, master):
        self.serve_counter = 0
        self.ip_addr = ip_addr
        self.port = 8080
        self.url = "Others on the same WiFi can type " + str(self.ip_addr) + ':' + str(self.port) + " into their browser to download the uploaded file. "
        self.filename = 'N/A'
        self.frame = Frame(master, width=5000, height=5000)
        self.frame.pack(fill=X, padx=100, pady=100,)
        self.url_label = Label(self.frame, text="%s" % self.url)
        #self.url_label = Label(self.frame, text="%s" % self.url).pack()
        self.upload = Button(master, text="Choose file", command=self.chooseFile).pack()  
        self.serve = Button(master, text="Upload file", command=self.threadServer).pack()  
        self.servedFilename = Label(self.frame, text="")
        self.servedFilename.pack()
        self.t1 = None

    """ Update the GUI to display the file to be uploaded. """
    def showUploadedFile(self):
        self.servedFilename.configure(text="%s" % self.filename)

    """ Use another thread to serve files.  The GUI runs on main thread.  """
    def threadServer(self):
        print("Serve Counter: ", self.serve_counter)
        if (self.serve_counter == 0):
            self.t1 = Thread(target=self.uploadFile)
            self.t1.start()
            self.serve_counter += 1
        else:
            self.serve_counter += 1
            print("Serve counter: ", self.serve_counter)
            self.t1.run()
        
        
    """ Upload PATH to IP_ADDR at PORT to the built-in http server. """
    def uploadFile(self):
        HOST_NAME, PORT_NUMBER = self.ip_addr, self.port
        self.httpd = BaseHTTPServer.HTTPServer((HOST_NAME, PORT_NUMBER), MyHandler)
        self.httpd.allow_reuse_address = True
        self.url_label.pack()
        print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
        try:
            self.httpd.serve_forever()
        except KeyboardInterrupt:
            pass
        self.httpd.server_close()
        print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)

    """ Set PATH to chosen uploaded destination. """
    def chooseFile(self):   # GET MORE STABLE SOLUTION
        while True:
            uploadedfilenames = askopenfilenames(multiple=True)
            if uploadedfilenames == '':
                return
            uploadedfiles = root.tk.splitlist(uploadedfilenames)
            if len(uploadedfiles)!=1:
               tkMessageBox.showinfo(message="Select one file!")
               return
            else:
                self.filename = uploadedfiles
                self.showUploadedFile()
                global path
                path = uploadedfiles[0]
                return

    """ User closed window. Shutdown GUI and server. """
    def on_closing(self):
        if (self.serve_counter > 0):
            print("Closed server")
            self.httpd.server_close()
        root.destroy()

path = None     # path to requested uploaded file
ip_addr = get_ip_addr()
root = Tk()
root.wm_title("Local File Share")
# frame1 = Frame(root, width=500, height=500, background="bisque")
# frame2 = Frame(root, width=50, height = 50, background="#b22222")

# frame1.pack(fill=None, expand=False)
# frame2.place(relx=.5, rely=.5, anchor="c")
app = App(root)
root.protocol("WM_DELETE_WINDOW", app.on_closing)
root.mainloop()
