#! /usr/bin/env python
# -*- coding: utf-8 -*-
# K'atun Website Backend
# This backend acts as an intermediary between the database and the end user, allowing for safe operations on the database.
# The intention of this design is to mitigate potential SQL injections into the database, causing corruption and/or data loss.

import cherrypy, os, webbrowser
from db_backend import DatabaseInterface
from mako.template import Template
from mako.lookup import TemplateLookup
from parser import Parser


class Katun_Website(object):
	
	def __init__(self, template_dir="/templates"):
		self.interface = DatabaseInterface()
		self.lookup = TemplateLookup(directories = [template_dir])
	
	def index(self):
		template = Template(filename="templates/katun_layout.html")
		return template.render_unicode(title="Index")
	index.exposed = True
	
	def music(self):
		template = Template(filename="templates/katun_layout.html")
		return template.render_unicode(title="Music Collection")#"Hello world inside of the MUSIC method.")
	music.exposed = True
	
	def duplicates(self):
		return "Hello world, inside of the DUPLICATES method."
	duplicates.exposed = True
	
	def playlists(self):
		return "Hello world, inside of the PLAYLISTS method."
	playlists.exposed = True
	
	def favorites(self):
		return "Hello world, inside of the FAVORITES method."
	favorites.exposed = True
		
	def load_music(self, location):
		'''Load music in from a user's local machine.
		
		It has to be a valid path, which we'll check in here (and subsequently raise an error or redirect).'''
		
		if not os.path.exists(location):
			raise Exception(u"Bogus location") # do something with it later
		p = Parser(location.strip())
		del p
		raise cherrypy.HTTPRedirect("index")
	load_music.exposed = True
		
		# May God have mercy on your soul if your collection is north of 5,000.

class Katun_Song(object):
	
	def song_url(self, title, **elements):
		'''Accept a full-blown song as a URL.'''
		template = Template(filename="")
		return template.render_unicode(elements)
		

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
