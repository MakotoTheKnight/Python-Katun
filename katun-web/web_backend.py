#! /usr/bin/env python
# -*- coding: utf-8 -*-
# K'atun Website Backend
# This backend acts as an intermediary between the database and the end user, allowing for safe operations on the database.
# The intention of this design is to mitigate potential SQL injections into the database, causing corruption and/or data loss.

import cherrypy, os, webbrowser
from mako.template import Template
from mako.lookup import TemplateLookup
from parser import Parser
from db_backend import DatabaseInterface


class Katun_Website(object):
	
	def __init__(self):
		self.lookup = TemplateLookup(directories = ["templates"])
		self.template = Template(filename="templates/katun_layout.html")
	
	def index(self):
		with open('templates/index.html', 'r') as f:
			return self.template.render_unicode(title="Index", content=f.read())
	index.exposed = True
	
	def music(self, query="select title, artist, album, genre, filetype, location from song;"):
		music_template = Template(filename="templates/music_table.html").render_unicode(sql=query)
		
		return self.template.render_unicode(title="Music Collection", content = music_template)#"Hello world inside of the MUSIC method.")
	music.exposed = True
	
	def duplicates(self):
		duplicates_template = Template(filename="templates/results_table.html").render(sql="select * from duplicates;")
		return self.template.render_unicode(title="Duplicates", content = duplicates_template)#"Hello world inside of the MUSIC method.")
	duplicates.exposed = True
	
	def playlists(self):
		return self.template.render_unicode(title="Playlists [BETA]", content = "Give me a minute.")#"Hello world inside of the MUSIC method.")
	playlists.exposed = True
	
	def favorites(self):
		return self.template.render_unicode(title="Favorites", content = "Give me a minute.")#"Hello world inside of the MUSIC method.")
	favorites.exposed = True
	
	def get_help(self):
		return self.template.render_unicode(title="Music Collection", content = "Give me a minute.")#"Hello world inside of the MUSIC method.")
	get_help.exposed = True
	
	def song(self, location):
		"""Retrieve the song from the database by its entryorder.  This is guaranteed to be a unique value."""
		location = unicode(location)
		db = DatabaseInterface()
		song = db.execute_query("select * from song where location = \"" + location +  "\";")
		results = dict(zip(song[0].keys(), song[0]))
		song_info = Template(filename="templates/song_information.html").render_unicode(kw=results)
		return self.template.render_unicode(title="Song Information", content=song_info)
	song.exposed = True
		
	def load_music(self, location):
		'''Load music in from a user's local machine.
		
		It has to be a valid path, which we'll check in here (and subsequently raise an error or redirect).'''
		
		if not os.path.exists(location):
			raise cherrypy.HTTPRedirect("index") # do something with it later
		p = Parser(location.strip(), startfresh=True)
		raise cherrypy.HTTPRedirect("music")
	load_music.exposed = True


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
