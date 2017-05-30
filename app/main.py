from Tkinter import *
import socket
from tkFileDialog import askopenfilenames
import tkFileDialog
import tkMessageBox
import pdb
import sys
sys.path.insert(0, '/media/sammy/Baracuda/ubuntu/documents/summer_17/Networking/local_sockets/modules')
from ip import get_ip_addr

class App:
    def __init__(self, master):
        self.ip_addr = ip_addr
        self.port = 8080
        self.url = str(self.ip_addr) + ':' + str(self.port)
        
        self.filenames = []
        self.frame = Frame(master)
        self.frame.pack(fill=X, padx=50, pady=50)


        self.upload = Button(master, text="Upload file", command=self.fileupload).pack()  

        self.hi_there = Button(self.frame, text="Hello", command=self.say_hi)
        self.hi_there.pack()
        self.servedFilename = Label(self.frame, text="")
        self.servedFilename.pack()

    def say_hi(self):
        print "hi there, everyone!"
        print("self upload: ", self.filenames) 
        # self.label.configure(text="%d" % self.ip_addr)
        # self.label.pack()

    def showUploadedFile(self):
        self.servedFilename.configure(text="%s" % self.filenames)
        print('showing uploaded file name')
        #self.servedFilename.configure(text="hi").pack()
        return

    def fileupload(self):
        while True:
            uploadedfilenames = askopenfilenames(multiple=True)
            if uploadedfilenames == '':
                tkMessageBox.showinfo(message="File Upload has been cancelled program will stop")
                return
            uploadedfiles = root.tk.splitlist(uploadedfilenames)
            if len(uploadedfiles)!=1:
               tkMessageBox.showinfo(message="Select at least one file!")
            else:
                if uploadedfiles not in self.filenames:
                    self.filenames.append(uploadedfiles)
                #serveFile(filenames[0][0])
                self.showUploadedFile()
                return uploadedfiles


# REWRITE
# this function to utlize Python's built in HTTP server and serve up just FILENAME
def serveFile(filename):
    port = 8080                    # Reserve a port for your service.
    # s = socket.socket()             # Create a socket object
    # host = ip_addr
    # s.bind((host, port))            # Bind to the port
    # s.listen(5)   
    # Label(master, textvariable=filename).pack()
    # while True:
    #     print('while true')
    #     display.configure(text="new file")
    #     print("uploading file ?")
    #     conn, addr = s.accept()     # Establish connection with client.
    #     print 'Got connection from', addr
    #     data = conn.recv(1024)
    #     print('Server received', repr(data))
    #     f = open(filename,'rb')

    #     l = f.read(1024)
    #     while (l):
    #        conn.send(l)
    #        print('Sent ',repr(l))
    #        l = f.read(1024)
    #     f.close()

    #     print('Done sending')
    #     conn.send('Thank you for connecting')
    #     conn.close()
    # s.close()
    # return




# get ip address
ip_addr = get_ip_addr()

root = Tk()
app = App(root)
root.mainloop()
root.destroy() # optional; destroys python process if not already done so
