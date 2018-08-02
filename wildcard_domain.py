#!/usr/bin/python
import uuid
import socket
import sys

prefix = uuid.uuid4()
domain = sys.argv[1]

wild = str(prefix) + "." + domain

try:
  print "Trying to resolve %s" % wild
  result = socket.gethostbyname(wild)
  print "%s resolves to %s" % (wild, result)
  print "%s has a wildcard DNS entry" % sys.argv[1]

except:
  print "%s does not have a wildcard DNS entry" % sys.argv[1]
