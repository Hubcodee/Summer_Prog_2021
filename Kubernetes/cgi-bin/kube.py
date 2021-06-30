#!/usr/bin/python3
import cgi

import test

print("content-type:text/html")
print()

app = cgi.FieldStorage()
cmd = app.getvalue('value')


test.process_str(cmd)
