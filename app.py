from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        message = "Hello from my Dockerized Python application!"

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        self.wfile.write(message.encode())

server = HTTPServer(("0.0.0.0", 8080), Handler)

print("Server running on port 8080")

server.serve_forever()
