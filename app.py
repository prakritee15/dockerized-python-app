from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(
            b"Hello from a Dockerized Python Application!"
        )

print("Starting server on port 8080...")
HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
