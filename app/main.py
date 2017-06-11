from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from Tkinter import *
from tkFileDialog import askopenfilenames
from ip import get_ip_addr
import time
from threading import Thread

""" Display landing webpage at IP_ADDR:PORT and allow download of PATH file. """
class MyHandler(BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(s):      #"""Respond to a GET request."""
        print("Path: ", filepaths)
        for file in filepaths:
            if (s.path == file):  # retrieve uploaded file
                print("Sending download...")
                s.send_response(200)
                s.send_header("Content-type", "multipart/form-data")
                s.end_headers()
                file = open(file, 'rb')
                l = file.read(1024)
                while(l):
                    s.wfile.write(l)
                    l = file.read(1024)
                file.close()
                return
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        s.wfile.write("<h3>Click on any of the files below to download them. </h3>")
        s.wfile.write("<ul>")
        for file in filepaths:
            s.wfile.write("<li><a href='{0}'>{0}</a></li>".format(file))
        s.wfile.write("</ul>")

""" The main GUI app. Initializes GUI window and button events. """
class App:
    def __init__(self, master):
        self.frame = Frame(master, width=5000, height=5000)
        self.serve_counter = 0
        self.ip_addr = ip_addr
        self.port = 8080
        self.url = "Others on the same WiFi can type " + str(self.ip_addr) \
            + ':' + str(self.port) + " into their browser to download the uploaded file. "
        self.url_label = Label(self.frame, text="%s" % self.url)
        self.filenames = 'N/A'
        self.frame.pack(fill=X, padx=100, pady=100,)
        self.upload = Button(master, text="Choose file", command=self.chooseFile).pack()  
        self.serve = Button(master, text="Upload file", command=self.threadServer).pack()  
        self.servedFilenames = Label(self.frame, text="")
        self.servedFilenames.pack()
        self.t1 = None    # server thread

    """ Update the GUI to display the file to be uploaded. """
    def showUploadedFile(self):
        self.servedFilenames.configure(text="%s" % str(self.filenames))

    """ Use another thread to serve files since the GUI runs on main thread.  """
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
        self.httpd = HTTPServer((HOST_NAME, PORT_NUMBER), MyHandler)
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
    def chooseFile(self):
        while True:
            uploadedfilenames = askopenfilenames(multiple=True)
            if uploadedfilenames == '':
                return
            uploadedfiles = root.tk.splitlist(uploadedfilenames)
            self.filenames = uploadedfilenames
            self.showUploadedFile()
            global filepaths
            filepaths = uploadedfiles
            return

    """ User closed window. Shutdown GUI and server. """
    def on_closing(self):
        if (self.serve_counter > 0):
            print("Closed server")
            self.httpd.server_close()
        root.destroy()

filepaths = None     # path for each file to be uploaded
ip_addr = get_ip_addr()
root = Tk()
root.wm_title("Local File Share")
app = App(root)
root.protocol("WM_DELETE_WINDOW", app.on_closing)
root.mainloop()
