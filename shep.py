#!/usr/bin/python
"""Simple HTTP Emulation in Python - SHEP

Tamper with HTTP headers to your heart's content. Excellent for 
testing, or just having a good time trying to break other tools.

"""
import SimpleHTTPServer
import SocketServer
import atexit
import os
import sys

#We will fall back to 8000
try:
  port = int(sys.argv[1])
except:
  port = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
Handler.sys_version = ""

#Let's redefine the default values to suit our purposes
try:
  Handler.server_version = sys.argv[2]
except:
  Handler.server_version = "Apache/2.2.3 PHP/5.1.6"


print "Server: " + Handler.server_version
print "Port  : " + str(port)

httpd = SocketServer.TCPServer(("", port), Handler)

httpd.serve_forever()
