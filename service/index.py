# coding=utf-8
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
from os import path
from bill import Bill


_DEFAULT_PORT = 9990
_CURDIR = path.dirname(path.realpath(__file__))


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        querypath = urlparse(self.path)
        filepath, query = querypath.path, querypath.query
        print(filepath)
        if filepath.endswith('/list'):
            bl = Bill()
            self._send_response(bl.get_list())
            return
        else:
            self.show_index()
            return
    
    def do_POST(self):
        if filepath.endswith('/add'):
            self._send_response('add')
            return
        raise Exception('todo')
    
    def show_index(self):
        with open(_CURDIR + '/../view/bill.html','r') as f:
            content = f.read()
            self._send_response(content)
    
    def _send_response(self, content, mimetype='text/html'):
        self.send_response(200)
        self.send_header('Content-type', mimetype)
        self.end_headers()
        self.wfile.write(str.encode(content))


def run_server(port=_DEFAULT_PORT):
    """
    run http server
    """
    server_addr = ('', port)
    httpd = HTTPServer(server_addr, RequestHandler)
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()
    pass
