#!/usr/bin/env python -W ignore

# Testing for library completeness

import cherrypy
from lib.mutagen import *
'''
class HelloWorld:
    def index(self):
	print "this isn't python 3."
        return "Hello world!"
    index.exposed = True

if __name__ == '__main__':
	print cherrypy.config, cherrypy.server
	cherrypy.quickstart(HelloWorld())'''
	
class Root:
    def mytest(self, entryorder):
		
        return repr(dict(entryorder=entryorder))
    mytest.exposed = True


if __name__ == '__main__':
    # CherryPy always starts with app.root when trying to map request URIs
    # to objects, so we need to mount a request handler root. A request
    # to '/' will be mapped to HelloWorld().index().
    cherrypy.quickstart(Root())
