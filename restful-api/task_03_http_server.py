#!/usr/bin/env python3
"""
Simple web server using http.server module

Handles:
- GET /           → plain text message
- GET /data       → JSON dataset
- GET /status     → plain OK response
- GET /info       → JSON with info metadata
- Any other route → 404 Not Found with error message
"""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer

# Sample datasets
SAMPLE_DATA = {"name": "John", "age": 30, "city": "New York"}
INFO_DATA = {"version": "1.0", "description": "A simple API built with http.server"}

class MyRequestHandler(BaseHTTPRequestHandler):
    """Custom HTTP request handler for GET endpoints."""

    def do_GET(self):
        """Handle GET requests based on the request path."""
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(SAMPLE_DATA).encode())

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(INFO_DATA).encode())

        else:
            self.send_response(404)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            error_message = {"error": "Endpoint not found"}
            self.wfile.write(json.dumps(error_message).encode())

    def log_message(self, format, *args):
        """Disable default logging (optional)."""
        return


def run_server(port=8000):
    """Start the HTTP server on the specified port."""
    server_address = ('', port)
    httpd = HTTPServer(server_address, MyRequestHandler)
    print(f"Serving on http://localhost:{port} ...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        httpd.server_close()


if __name__ == "__main__":
    run_server()

