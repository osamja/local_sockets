# Given a path to a file, serve that file. 
import time
import BaseHTTPServer


# HOST_NAME = 'example.net' # !!!REMEMBER TO CHANGE THIS!!!
HOST_NAME = 'localhost'
PORT_NUMBER = 8088
url = "Problem.mp3"

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(s):
        """Respond to a GET request."""
        if (s.path == "/" + str(url)):
            print("same url")
            s.send_response(200)
            s.send_header("Content-type", "multipart/form-data")
            s.end_headers()
            file = open(url, 'rb')
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
        s.wfile.write("%s" % url)
        s.wfile.write(">file</a>")


if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)
