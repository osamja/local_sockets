from Tkinter import *
import socket
from tkFileDialog import askopenfilenames
import tkFileDialog
import tkMessageBox

# get ip address
ip_addr = ([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('192.168.2.1', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]) + ':8080'
print("My ip addr is: ", ip_addr)

# setup GUI

master = Tk()
ip = StringVar(master)
ip.set(ip_addr)



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
            return uploadedfiles



Label(master, textvariable=ip).pack()
separator = Frame(height=500, width=500, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=5, pady=5)

Button(master, text="Upload file", command=fileupload).pack()

mainloop()