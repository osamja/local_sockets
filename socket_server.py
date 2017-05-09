import socket

s = socket.socket()	# create socket object
#host = socket.gethostname()
host = '192.168.1.165'
port = 12345
s.bind((host, port))
s.listen(5)
while True:
	c, addr = s.accept()
	print("Got connection from ", addr)
	c.send("Thank you for connecting")
	c.close()
