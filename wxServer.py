#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: hollay
# @Date:   2018--18 20:50:
# @Last Modified by:   hollay
# @Last Modified time: 2018--18 20:50:

import sys
import BaseHTTPServer
from StringIO import StringIO
from SimpleHTTPServer import SimpleHTTPRequestHandler
ServerClass  = BaseHTTPServer.HTTPServer
Protocol     = 'HTTP/1.0'

class WeServer(SimpleHTTPRequestHandler):
    def __init__(self, req, client_addr, server):
        SimpleHTTPRequestHandler.__init__(self, req, client_addr, server)

    def do_HEAD(self):
        self.do_GET()
    def do_GET(self):
        str = 'Hello World'

        self.send_response(200)

        self.send_header('Content-Type', 'text/plain')
        self.send_header('Content-Length', len(str))
        self.end_headers()

        self.wfile.write(str)

if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 10243

server_address = ('127.0.0.1', port)
WeServer.protocol_version = Protocol
httpd = ServerClass(server_address, WeServer)

sa = httpd.socket.getsockname()
print 'Serving HTTP on ', sa[0], 'port: ', sa[1], '...'
httpd.serve_forever()