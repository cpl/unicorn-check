import sys
import re
import os

if __name__ == "__main__":
    unicorn = 0
    if os.path.isfile(sys.argv[1]):
        with open(sys.argv[1], 'r') as unicorn_file:
            for line in unicorn_file.readlines():
                unistring = unicode(line, 'utf-8')
                unistring = unistring.encode('unicode_escape')
                unicorn += len(re.findall('\U0001f984', unistring))

    if unicorn > 0:
        print "You have " + str(unicorn) + " unicorn/s in your file."
