#! /usr/bin/env python
# -*- coding: utf-8 -*-
# K'atun Website Backend
# This backend acts as an intermediary between the database and the end user, allowing for safe operations on the database.
# The intention of this design is to mitigate potential SQL injections into the database, causing corruption and/or data loss.

import cherrypy, os, webbrowser
from db_backend import DatabaseInterface
from mako.template import Template
from parser import Parser


class Katun_Website(object):
	
	def __init__(self):
		self.interface = DatabaseInterface()
	
	@cherrypy.expose
	def index(self):
		template = Template(filename="templates/Katun_Index.html")
		return template.render_unicode(title="Index")
	
	@cherrypy.expose
	def music(self):
		return "Hello world inside of the MUSIC method."
	
	@cherrypy.expose
	def duplicates(self):
		return "Hello world, inside of the DUPLICATES method."
	
	@cherrypy.expose
	def playlists(self):
		return "Hello world, inside of the PLAYLISTS method."
	
	@cherrypy.expose
	def favorites(self):
		return "Hello world, inside of the FAVORITES method."

def main():
	'''main() functions are used to test the validity and performance of the module alone.
	This function is to NEVER be called outside of testing purposes.'''
	
	conf = {
		'/':
			{'tools.staticdir.root': os.path.dirname(os.path.abspath(__file__))},
		'/templates':
		{
			'tools.staticfile.on': True,
			'tools.staticfile.filename': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates/katun.css')
		}
	}
	
	cherrypy.quickstart(Katun_Website(), config=conf)
	
if __name__ == '__main__':
	main()
