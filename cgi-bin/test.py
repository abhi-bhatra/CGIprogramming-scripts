#!/usr/bin/python

import cgi
import subprocess

print("content-type: text/html")
print()

form = cgi.FieldStorage()
cmd=form.getValue("state")

print(f'The value of state is {state}')
