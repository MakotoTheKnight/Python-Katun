#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Katun SQLite Backend
# This backend acts as an intermediary between the database and the true middleware, allowing for safe operations on the database.
# The intention of this design is to mitigate potential SQL injections into the database, causing corruption and/or data loss.

__all__ = ['DatabaseInterface']

import sqlite3, os

__metaclass__ = type

class DatabaseInterface:
	'''Specify the SQLite backend interface to the website.
	
	We know where the database is stored within the file structure, but if it doesn't exist, we can re-create it here.
	The schema with which we create and populate the database, including triggers, is defined elsewhere.'''

	def __init__(self, db_path="../Katun.db"):
		self.db_path = db_path
		self.connection = sqlite3.connect(db_path)
		self.cursor = self.connection.cursor()

	def reset_database(self):
		'''"Reset" the database. 

		This operation deletes the db file associated with K'atun.'''
		
		os.remove(self.db_path)
		self.__build_database()

	def __build_database(self):
		"""Build the database.
		
		This operation is valid only after reset_database() is called, otherwise, undefined behavior may occur."""
		
		self.connect = sqlite3.connect(self.db_path)
		self.cursor = self.connect.cursor()
		with open('../tables.sql', encoding='utf_8', 'r') as f:
			self.cursor.executescript(f.read())
			self.connection.commit()

	def commit(self):
		"""A common interface for committing changes to the database.
		This interface is to be used outside of the scope of this object; i.e. when another object or method cannot reach the Connection object."""
	
		self.connection.commit()
		
	def rollback(self):
		"""A common interface for rolling changes back to the database.
		This interface is to be used outside of the scope of this object; i.e. when another object or method cannot reach the Connection object."""

		self.connection.rollback()
	
	def check_valid_sql(self, sql):
		"""Check if a statement is, indeed, valid SQL.  Follows the specifications of sqlite3.complete_statement()."""
		pass
	
	def execute_sql(self, sql):
		"""Execute a valid SQL statement.
		
		We first check to see if it is valid SQL, and if it isn't, we pass through a sqlite3.Error which is to be handled from the caller.
		Upon successful validation, we execute the statement.  If an error occurs, we pass the error back to the caller."""
		
		pass

	def execute_batch_sql(self, sql, *statements):
		"""Execute multiple, valid SQL statements.
		
		We check to see if it is valid SQL, as with execute_sql.  We allow the statements through if they are valid.  All errors are passed to the caller."""
		self.cursor.executemany(unicode(sql, 'utf_8'), statements)
