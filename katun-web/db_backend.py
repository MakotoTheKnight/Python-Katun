#! /usr/bin/env python
# -*- coding: utf-8 -*-
# K'atun SQLite Backend
# This backend acts as an intermediary between the database and the true middleware, allowing for safe operations on the database.
# The intention of this design is to mitigate potential SQL injections into the database, causing corruption and/or data loss.

__all__ = ['DatabaseInterface', 'DatabaseError']

import sqlite3, exceptions, os

__metaclass__ = type

class DatabaseError(Exception): pass

class DatabaseInterface:
	'''Specify the SQLite backend interface to the website.
	
	We know where the database is stored within the file structure, but if it doesn't exist, we can re-create it here.
	The schema with which we create and populate the database, including triggers, is defined elsewhere.'''

	def __init__(self, db_path="../db/Katun.db"):
		self.db_path = db_path

	def reset_database(self):
		'''"Reset" the database. 

		This operation deletes the db file associated with K'atun.'''
		if os.path.exists(self.db_path):
			os.remove(self.db_path)
		
		self.__build_database()

	def __build_database(self):
		"""Build the database.
		
		This operation is valid only after reset_database() is called, otherwise, undefined behavior may occur."""
		
		with open('../db/tables.sql', 'r') as f:
			with sqlite3.connect(self.db_path) as con:
				con.executescript(f.read())
				con.commit()

	def commit(self):
		"""A common interface for committing changes to the database.
		This interface is to be used outside of the scope of this object; i.e. when another object or method cannot reach the Connection object."""
	
		self.connection.commit()

	def rollback(self):
		"""A common interface for rolling changes back to the database.
		This interface is to be used outside of the scope of this object; i.e. when another object or method cannot reach the Connection object."""

		self.connection.rollback()
	
	def execute_query(self, sql):
		"""Execute a valid SQL query.
		
		We first check to see if it is valid SQL, and if it isn't, we pass through a sqlite3.Error which is to be handled from the caller.
		Upon successful validation, we execute the statement.  If an error occurs, we pass the error back to the caller."""
		
		if not sqlite3.complete_statement(sql):
			raise DatabaseError(u"The statement you provided isn't valid SQL.")
		
		if "update" in sql or "delete" in sql or "insert" in sql:
			raise DatabaseError(u"Incorrect method; please use either\"execute_insert_statement\" or \"execute_update_statement()\" or \"execute_delete_statement()\" instead.")
		
		with sqlite3.connect(self.db_path) as con:
			con.row_factory = sqlite3.Row
			cur = con.cursor()
			cur.execute(sql)
			return cur.fetchall()

	def execute_insert_statement(self, sql, parameters):
		"""Execute a valid SQL insert statement using qmark notation.
		
		We first check to see if it is valid SQL, and if it isn't, we pass through a sqlite3.Error which is to be handled from the caller.
		Upon successful validation, we execute the statement.  If an error occurs, we pass the error back to the caller."""
		
		if not '?' in sql:
			raise DatabaseError(u"The SQL statement provided didn't contain qmark notation.")
		if "update" in sql or "delete" in sql or "select" in sql:
			raise DatabaseError(u"Incorrect method; please use either\"execute_insert_statement\" or \"execute_update_statement()\" or \"execute_query()\" instead.")
			
		with sqlite3.connect(self.db_path) as con:
			try:
				con.execute(sql, parameters)
			except Exception, e:
				print e.__unicode__()

	def execute_update_statement(self, sql, parameters):
		"""Execute a valid SQL update statement using qmark notation.
		
		We first check to see if it is valid SQL, and if it isn't, we pass through a sqlite3.Error which is to be handled from the caller.
		Upon successful validation, we execute the statement.  If an error occurs, we pass the error back to the caller."""
		
		if not '?' in sql:
			raise DatabaseError(u"The SQL statement provided didn't contain qmark notation.")
		
		if "insert" in sql or "delete" in sql or "select" in sql:
			raise DatabaseError(u"Incorrect method; please use either\"execute_insert_statement()\" or \"execute_query()\" or \"execute_delete_statement()\" instead.")	
		
		with sqlite3.connect(self.db_path) as con:
			try:
				con.execute(sql, parameters)
			except Exception, e:
				print e.__unicode__()

	def execute_delete_statement(self, sql, parameters):
		"""Execute a valid SQL delete statement using qmark notation.
		
		We first check to see if it is valid SQL, and if it isn't, we pass through a sqlite3.Error which is to be handled from the caller.
		Upon successful validation, we execute the statement.  If an error occurs, we pass the error back to the caller."""
		
		if not '?' in sql:
			raise DatabaseError(u"The SQL statement provided didn't contain qmark notation.")
		
		if "update" in sql or "insert" in sql or "select" in sql:
			raise DatabaseError(u"Incorrect method; please use either\"execute_insert_statement()\" or \"execute_update_statement()\" or \"execute_query()\" instead.")
		
		with sqlite3.connect(self.db_path) as con:
			try:
				con.execute(sql, parameters)
			except Exception, e:
				print e.__unicode__()

	def execute_batch_insert_statement(self, sql, statements):
		"""Execute a batch-oriented SQL statement using qmark notation."""
		if not '?' in sql:
			raise DatabaseError(u"The SQL statement provided didn't contain qmark notation.")
		
		with sqlite3.connect(self.db_path) as con:
			try:
				print "Committing..."
				con.executemany(sql, statements)
				con.commit()
			except Exception, e:
				print e.__unicode__()
				
def main():
	'''main() functions are used to test the validity and performance of the module alone.
	This function is to NEVER be called outside of testing purposes.'''
	try:
		db = DatabaseInterface()
		info = db.execute_query('select title, artist, album, genre, filetype from song;')
		keys = info[0].keys()
		print keys
		for line in info:
			print line
		
	except Exception, e:
		print e.__unicode__()

if __name__ == '__main__': main()
