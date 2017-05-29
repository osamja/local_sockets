from Tkinter import *
import socket
from tkFileDialog import askopenfilenames
import tkFileDialog
import tkMessageBox
import pdb

# get ip address
ip_addr = ([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('192.168.2.1', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0])
print("My ip addr is: ", ip_addr)

# setup GUI

master = Tk()
ip = StringVar(master)
ip.set(ip_addr)

filenames = []

def fileupload():
    while True:
        uploadedfilenames = askopenfilenames(multiple=True)
        if uploadedfilenames == '':
            tkMessageBox.showinfo(message="File Upload has been cancelled program will stop")
            return
        uploadedfiles = master.tk.splitlist(uploadedfilenames)
        if len(uploadedfiles)!=1:
           tkMessageBox.showinfo(message="Select at least one file!")
        else:
            print("sucessfully uploaded this file")
            filenames.append(uploadedfiles)
            serveFile(filenames[0][0])
            return uploadedfiles

def serveFile(filename):
    port = 8080                    # Reserve a port for your service.
    s = socket.socket()             # Create a socket object
    host = ip_addr
    print("host: ", host)
    print("filename: ", filename)
    s.bind((host, port))            # Bind to the port
    s.listen(5)   
    while True:
        print('while true')
        conn, addr = s.accept()     # Establish connection with client.
        print 'Got connection from', addr
        data = conn.recv(1024)
        print('Server received', repr(data))
        f = open(filename,'rb')

        l = f.read(1024)
        while (l):
           conn.send(l)
           print('Sent ',repr(l))
           l = f.read(1024)
        f.close()

        print('Done sending')
        conn.send('Thank you for connecting')
        conn.close()
    return

Label(master, textvariable=ip).pack()
separator = Frame(height=500, width=500, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=5, pady=5)
Button(master, text="Upload file", command=fileupload).pack()

mainloop()

