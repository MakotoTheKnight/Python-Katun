#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Katun Website Backend
# This backend acts as an intermediary between the database and the end user, allowing for safe operations on the database.
# The intention of this design is to mitigate potential SQL injections into the database, causing corruption and/or data loss.

import lib.web as web, exceptions

__metaclass__ = type

urls = (
	'/', 'Index',
	'/music', 'Music',
	'/music/duplicates', 'Duplicates',
	'/playlists', 'Playlists',
	'/favorites', 'Favorites'
	
)
app = web.application(urls, globals())

class Index:
	'''Define the index class.  We'll focus on making it pretty later.'''
	
	def GET(self):
		return "Hello world!"
		
class Music:
	'''Define the Music class.  We'll focus on making it pretty later.'''
	
	def GET(self):
		return "Hello warld!"
		
class Duplicates:
	'''Define the Duplicates class.  We'll focus on making it pretty later.'''
	
	def GET(self):
		return "Hello werld!"
		
class Playlists:
	'''Define the Playlists class.  We'll focus on making it pretty later.'''
	
	def GET(self):
		return "Hello wurld!"
		
class Favorites:
	'''Define the Favorites class.  We'll focus on making it pretty later.'''
	
	def GET(self):
		return "Hello woorld!"


class DatabaseInterface:
	'''Specify the SQLite backend interface to the website.
	
	We know where the database is stored within the file structure, but if it doesn't exist, we can re-create it here.
	The schema with which we create and populate the database, including triggers, is defined elsewhere.'''

	def __init__(self, db="../Katun.db"):
		self.db = db


class HTMLError(Exception):
	'''Specify a flexible HTML error.
	The sorts of errors recognized are 404 and 403.'''
	pass

def main():
	app.run()
	
if __name__ == '__main__':
	main()
