#! /usr/bin/env python
# -*- coding: utf-8 -*-
# K'atun Website Backend
# This backend acts as an intermediary between the database and the end user, allowing for safe operations on the database.
# The intention of this design is to mitigate potential SQL injections into the database, causing corruption and/or data loss.

import cherrypy, os
from mako.template import Template
from mako.lookup import TemplateLookup
from katun_backend.parser import Parser
from katun_backend.db_backend import DatabaseInterface


class Katun_Website(object):
	
	def __init__(self):
		self.lookup = TemplateLookup(directories = ["templates"])
		self.template = Template(filename="templates/katun_layout.html")
	
	@cherrypy.expose
	def index(self):
		'''Control the index page.'''
		with open('templates/index.html', 'r') as f:
			return self.template.render_unicode(title="Index", content=f.read())
	
	@cherrypy.expose
	def music(self, query="select title, artist, album, genre, filetype, location from song;"):
		'''Control the main Music layout page.'''
		music_template = Template(filename="templates/music_table.html").render_unicode(sql=query)
		
		return self.template.render_unicode(title="Music Collection", content = music_template)#"Hello world inside of the MUSIC method.")
	
	@cherrypy.expose
	def duplicates(self):
		'''Control the main Duplicates layout page.'''
		try:
			duplicates_template = Template(filename="templates/results_table.html").render_unicode(sql="select * from duplicates;")
			return self.template.render_unicode(title="Duplicates", content = duplicates_template)
		except:
			return self.template.render_unicode(title="Duplicates", content = "You don't have any duplicates in your music collection!  Lucky you!")
	
	@cherrypy.expose
	def playlists(self):
		'''Control the main Playlists layout page.'''
		try:
			playlist_template = Template(filename="templates/playlist_table.html").render_unicode(sql="select * from playlist;")
			return self.template.render_unicode(title="Playlists [BETA]", content = playlist_template)
		except:
			return self.template.render_unicode(title="Playlists [BETA]", content = """
			
			You haven't created any playlists yet.
			<form action = "create_playlist" enctype="multipart/form-data/" method = "post">
				<input type="text" name="name" size="60">
			</form>
			
			""")
	
	@cherrypy.expose
	def favorites(self):
		'''Control the main Favorites layout page.'''
		try:
			favorites_template = Template(filename="templates/results_table.html").render_unicode(sql="select * from favorites;")
			return self.template.render_unicode(title="Favorites", content = favorites_template)
		except:
			return self.template.render_unicode(title="Favorites", content = "No favorites added yet.  If you want to add them, you have to click on the individual song.")
	
	@cherrypy.expose
	def get_help(self):
		'''Control the main help page.'''
		help_template = Template(filename="templates/help.html").render_unicode()
		return self.template.render_unicode(title="Help", content = help_template)
	
	@cherrypy.expose
	def song(self, location):
		"""Retrieve the song from the database by its physical location."""
		location = unicode(location)
		db = DatabaseInterface()
		song = db.execute_query("select * from song where location = \"" + location +  "\";")
		results = dict(zip(song[0].keys(), song[0]))
		song_info = Template(filename="templates/song_information.html").render_unicode(kw=results)
		return self.template.render_unicode(title="Song Information", content=song_info)

	@cherrypy.expose
	def load_music(self, location):
		'''Load music in from a user's local machine.
		
		It has to be a valid path, which we'll check in here (and subsequently raise an error or redirect).'''
		
		if not os.path.exists(location):
			raise cherrypy.HTTPRedirect("index") # do something with it later
		p = Parser(location.strip(), startfresh=True)
		raise cherrypy.HTTPRedirect("music")
		
	@cherrypy.expose
	def add_favorite(self, location, artist, filetype, title):
		'''Insert a new favorite into the database.'''
		db = DatabaseInterface()
		params = (1, location, artist, filetype, title)
		db.execute_insert_statement("insert into favorites(uid, location, artist, filetype, title) VALUES (?, ?, ?, ?, ?)", params)
		raise cherrypy.HTTPRedirect(u"song?location=" + location)
	
	@cherrypy.expose	
	def create_playlist(self, name):
		'''Create a playlist and insert it into the database.'''
		db = DatabaseInterface()
		params = (name, 1, None)
		db.execute_insert_statement("insert into playlist(pname, uid, count) VALUES (?, ?, ?)", params)
		raise cherrypy.HTTPRedirect("playlists")
		
	@cherrypy.expose
	def query_playlist(self, pname):
		'''Retrieve elements of a playlist by its name.'''
		try:
			favorites_template = Template(filename="templates/results_table.html").render_unicode(sql="select title, artist from contains where pname = \"" + pname + "\";")
			return self.template.render_unicode(title="Playlist " + pname, content = favorites_template)
		except:
			return self.template.render_unicode(title="Error", content = "This playlist doesn't have any elements inserted into it.")
	
	@cherrypy.expose
	def add_to_playlist(self, pname, location, artist, filetype, title):
		'''Insert an individual song into a playlist.'''
		params = (pname, location, artist, filetype, title)
		db = DatabaseInterface()
		try:
			db.execute_insert_statement("insert into contains (pname, location, artist, filetype, title) VALUES (?, ?, ?, ?, ?)", params)
		except:
			pass
		finally:
			raise cherrypy.HTTPRedirect(u"song?location=" + location)
		
	@cherrypy.expose
	def query_db(self, query):
		'''Run a query on the database (select statements only).'''
		try:
			query_template = Template(filename="templates/results_table.html").render_unicode(sql=query)
			return self.template.render_unicode(title="Query Results", content=query_template)
		except:
			return self.template.render_unicode(title="Query Results", content="Invalid query, please try again.")


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


#! /usr/bin/env python

'Example errors caught by PyChecker'

import string

metaslash = 1

def printNames():
    neal = 'neal'
    michelle = 'michele'
    eric = 5
    print "Local values: %(neal)S %(michele)s %(eric)" % locals()


class Nothing:
    def printValue(value):
        print value

    def set(self, value):
        self.value = value


def tryToDoSomething(self, value):
    try:
        import string

        if not value:
            raise RuntimeError, "Hey, there's no value"
        printNames('a, b, c')
    except:
        traceback.print_exc()


def setGlobal(value=None):
    print 'Old MetaSlash value is:', metaslash
    metaslash = value
    useless = Nothing(5)
    print 'a useless value is:', useless.valeu
