#!/usr/bin/env python -W ignore

# Testing for library completeness

import cherrypy
from lib.mutagen import *

class HelloWorld:
    def index(self):
	print "this isn't python 3."
        return "Hello world!"
    index.exposed = True

if __name__ == '__main__':
	print cherrypy.config, cherrypy.server
	cherrypy.quickstart(HelloWorld())
