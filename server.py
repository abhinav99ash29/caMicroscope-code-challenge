from http.server import HTTPServer, BaseHTTPRequestHandler
import cv2
import json
import numpy as np
import pickle
import base64



class S(BaseHTTPRequestHandler):
    img = cv2.imread('img1.jpeg')
    b,g,r = cv2.split(img)
    
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def _html(self, message):
        message = np.array(message)
        w,h = message.shape
        message = message.tolist()
        content = json.dumps({'w':w,'h':h,'data':list(message)})
        return content.encode('utf-8')
    def do_GET(self):
        self._set_headers()
        self.wfile.write(self._html('Hello GET!'))

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        post_data = post_data.decode('utf-8')
        self._set_headers()
        if post_data == 'b':
            self.wfile.write(self._html(self.b))
        if post_data == 'g':
            self.wfile.write(self._html(self.g))
        if post_data == 'r':
            self.wfile.write(self._html(self.r))


def run(server_class=HTTPServer, handler_class=S, addr="localhost", port=30000):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)

    print('Starting httpd server on {0}:{1}'.format(addr,port))
    httpd.serve_forever()


if __name__ == "__main__":
    run(addr='127.0.0.1', port=30000)