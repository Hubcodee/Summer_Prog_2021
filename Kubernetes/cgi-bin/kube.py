#!/usr/bin/python3
import cgi

import test

print("content-type:text/html")
print()

app = cgi.FieldStorage()
cmd = app.getvalue('value')


ret = test.process_str(cmd)
