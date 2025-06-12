#!/usr/bin/python3

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        if self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
             self.send_response(404)
             self.send_header("Content-type", "text/html")
             self.end_headers()
             self.wfile.write(b"Oops! Page not found.")

    #  start the web server

def run():
    server_address = ("", 8000)  #  port 8000

    httpd = HTTPServer(server_address, MyHandler)
    httpd.serve_forever()

if __name__ == '__main__':
        run()
