#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Katun Website Backend
# This backend acts as an intermediary between the database and the end user, allowing for safe operations on the database.
# The intention of this design is to mitigate potential SQL injections into the database, causing corruption and/or data loss.

import lib.web as web

__metaclass__ = type

class HTMLInterface:
	'''Specify the HTML specific interface to the website.
	We allow our structure to appear like this:
	
	/
	--/music
	----/duplicates
	--/playlists
	--/favorites'''
	
	def __init__(self):
		pass


class DatabaseInterface:
	'''Specify the SQLite backend interface to the website.
	
	We know where the database is stored within the file structure, but if it doesn't exist, we can re-create it here.
	The schema with which we create and populate the database, including triggers, is defined elsewhere.'''

	def __init__(self, db="../Katun.db"):
		self.db = db


class HTMLError(Exeception):
	'''Specify a flexible HTML error.
	The sorts of errors recognized are 404 and 403.'''
	pass
