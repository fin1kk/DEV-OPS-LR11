"""Simple module for DEV-OPS demo with a testable class. Change for test"""

import http.server
import socketserver

PORT = 8000


class TestMe:
    """A simple class to demonstrate testing and linting compliance."""

    def take_five(self):
        """Return the integer 5."""
        return 5

    def port(self):
        """Return the default server port."""
        return PORT


if __name__ == '__main__':
    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()
