#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Katun SQLite Backend
# This backend acts as an intermediary between the database and the true middleware, allowing for safe operations on the database.
# The intention of this design is to mitigate potential SQL injections into the database, causing corruption and/or data loss.

__all__ = ['DatabaseInterface']

class DatabaseInterface:
	'''Specify the SQLite backend interface to the website.
	
	We know where the database is stored within the file structure, but if it doesn't exist, we can re-create it here.
	The schema with which we create and populate the database, including triggers, is defined elsewhere.'''

	def __init__(self, db_path="../Katun.db"):
		self.db_path = db_path
		self.connect = sqlite3.connect(db_path)
		self.cursor = self.connect.cursor()

	@staticmethod
	def reset_database():
		'''Reset the database for new entries, or to clear something out.  Should only be used with the greatest of care.'''
		self.cursor.execute("DROP TABLE song")
		self.cursor.execute("DROP TABLE favorites")
		self.cursor.execute("DROP TABLE user")
		self.cursor.execute("DROP TABLE playlist")
		self.cursor.execute("DROP TABLE album")
		self.cursor.execute("DROP TABLE duplicates")
		self.cursor.execute("DROP TABLE contains")
		self.connect.commit()
		DatabaseInterface.build_database()

	@staticmethod
	def build_database():
		"""Rebuild the database for new entries.  Valid only after reset_database() is called, otherwise, undefined behavior
		may occur."""
		
		with open("../tables.sql", 'r') as f:
			pass
			
		
