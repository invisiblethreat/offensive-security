#!/usr/bin/python
import uuid
import socket
import sys

prefix = uuid.uuid4()
domain = sys.argv[1]

try:
  result = socket.gethostbyname(str(prefix) + "." + domain)
  print "%s has a wildcard DNS entry" % sys.argv[1]

except:
  print "%s does not have a wildcard DNS entry" % sys.argv[1]
