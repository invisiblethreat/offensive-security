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


def cleanup(dir):
  """Remove the directory we created on startup. 

  This is to be used in conjunction with atexit, which is called on a
  system interrupt. 
  """
  print "Removing directory: " + dir
  os.rmdir(dir)
  print "Exiting...\n"


def tmp_dir(dir):
  """Make a new empty directory for starting the server.

  The default action of SimpleHTTPServer is start in the working
  directory, which may contain other files or directories that we do 
  not want to be exposed for testing purposes. 
  """
  if os.path.exists(dir):
    print "The directory exists, aborting"
    sys.exit()
  else:
    print "Making: " + dir
    os.makedirs(dir)
    print "Changing to: " + dir
    os.chdir(dir)

#We will fall back to 8000
try:
  port = int(sys.argv[1])
except:
  port = 8000

dir = "/tmp/serve-" + str(port)

tmp_dir(dir)
atexit.register(cleanup, dir)

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
