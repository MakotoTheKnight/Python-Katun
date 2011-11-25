#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Katun SQLite Backend
# This backend acts as an intermediary between the database and the true middleware, allowing for safe operations on the database.
# The intention of this design is to mitigate potential SQL injections into the database, causing corruption and/or data loss.

__all__ = ['DatabaseInterface']

import sqlite3, os

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
		'''"Reset" the database. 

		This operation deletes the db file associated with K'atun.'''
		
		os.remove(self.db_path)
		DatabaseInterface.build_database()

	@staticmethod
	def build_database():
		"""Rebuild the database for new entries.  Valid only after reset_database() is called, otherwise, undefined behavior
		may occur."""
		
		self.connect = sqlite3.connect(self.db_path)
		self.cursor = self.connect.cursor()
		self.connect.execute("""P""")
		
		self.connect.executescript("""
		
		PRAGMA foreign_keys=ON;
		BEGIN TRANSACTION;

		/* Schemas */
		CREATE TABLE song(
			location TEXT,
			artist TEXT,
			filetype TEXT,
			title TEXT,
			genre TEXT,
			track INTEGER,
			album TEXT,
			bitrate INTEGER,
			year TEXT,
			entryorder INTEGER,
			--month INTEGER,
			PRIMARY KEY(
				location,
				artist,
				filetype,
				title
			)
		);

		CREATE TABLE user(
			uid INTEGER PRIMARY KEY AUTOINCREMENT,
			uname TEXT,
			password TEXT
		);

		CREATE TABLE contains(
			pname TEXT,
			location TEXT,
			artist TEXT,
			filetype TEXT,
			title TEXT,
			FOREIGN KEY(pname) REFERENCES playlist(pname),
			FOREIGN KEY(location, artist, filetype, title) REFERENCES song(location, artist, filetype, title)
		);

		CREATE TABLE favorites(
			uid INTEGER,
			location TEXT,
			artist TEXT,
			filetype TEXT,
			title TEXT,
			FOREIGN KEY(location, artist, filetype, title) references song(location, artist, filetype, title),
			FOREIGN KEY(uid) REFERENCES user(uid)
		);

		CREATE TABLE duplicates(
			location TEXT,
			artist TEXT,
			filetype TEXT,
			title TEXT,
			--duplicate_location TEXT PRIMARY KEY,
			FOREIGN KEY(location, artist, filetype, title) references song(location, artist, filetype, title)
		);

		CREATE TABLE playlist(
			pname TEXT PRIMARY KEY,
			uid INTEGER,
			count INTEGER,
			FOREIGN KEY(uid) REFERENCES user(uid)
		);

		CREATE TABLE album(
			location TEXT,
			artist TEXT,
			filetype TEXT,
			title TEXT,
			album_art_filename TEXT PRIMARY KEY,
			track_count INTEGER,
			FOREIGN KEY(location, artist, filetype, title) references song(location, artist, filetype, title)
		);

		/* Triggers */

		CREATE TRIGGER updateLocation AFTER UPDATE OF location on song FOR EACH ROW
		BEGIN
			UPDATE favorites
			SET location = new.location
			WHERE favorites.location = old.location;
			
			UPDATE album
			SET location = new.location
			WHERE album.location = old.location;
			
			UPDATE duplicates
			SET location = new.location
			WHERE duplicates.location = old.location;
			
			UPDATE contains
			SET location = new.location
			WHERE contains.location = old.location;
		END; 

		CREATE TRIGGER updateArtist AFTER UPDATE OF artist on song FOR EACH ROW
		BEGIN
			UPDATE favorites
			SET artist = new.artist
			WHERE favorites.artist = old.artist;
			
			UPDATE album
			SET artist = new.artist
			WHERE album.artist = old.artist;
			
			UPDATE duplicates
			SET artist = new.artist
			WHERE duplicates.artist = old.artist;
			
			UPDATE contains
			SET artist = new.artist
			WHERE contains.artist = old.artist;
		END; 

		CREATE TRIGGER updateTitle AFTER UPDATE OF title on song FOR EACH ROW
		BEGIN
			UPDATE favorites
			SET title = new.title 
			WHERE favorites.title = old.title;
			
			UPDATE album
			SET title = new.title 
			WHERE album.title = old.title;
			
			UPDATE duplicates
			SET title = new.title 
			WHERE duplicates.title = old.title;
			
			UPDATE contains
			SET title = new.title 
			WHERE contains.title = old.title;
		END; 

		CREATE TRIGGER updateFiletype AFTER UPDATE OF filetype on song FOR EACH ROW
		BEGIN
			UPDATE favorites
			SET filetype = new.filetype
			WHERE favorites.filetype = old.filetype;
			
			UPDATE album
			SET filetype = new.filetype
			WHERE album.filetype = old.filetype;
			
			UPDATE duplicates
			SET filetype = new.filetype
			WHERE duplicates.filetype = old.filetype;
			
			UPDATE contains
			SET filetype = new.filetype
			WHERE contains.filetype = old.filetype;
		END;

		CREATE TRIGGER deleteSong BEFORE DELETE ON song FOR EACH ROW
		BEGIN
			DELETE FROM album
			WHERE old.location = album.location
			AND old.artist = album.artist
			AND old.filetype = album.filetype
			AND old.title = album.title;
			
			DELETE FROM favorites
			WHERE old.location = favorites.location
			AND old.artist = favorites.artist
			AND old.filetype = favorites.filetype
			AND old.title = favorites.title;
			
			DELETE FROM duplicates
			WHERE old.location = duplicates.location
			AND old.artist = duplicates.artist
			AND old.filetype = duplicates.filetype
			AND old.title = duplicates.title;
			
			DELETE FROM contains
			WHERE old.location = contains.location
			AND old.artist = contains.artist
			AND old.filetype = contains.filetype
			AND old.title = contains.title;
		END;

		CREATE TRIGGER checkDuplicates AFTER INSERT ON song FOR EACH ROW
		BEGIN
			INSERT INTO duplicates (location, artist, filetype, title)
				SELECT location, artist, filetype, title
				FROM song
				WHERE artist = new.artist
				AND filetype = new.filetype
				AND title = new.title
				AND location <> new.location
				AND new.entryorder > entryorder;
		END;

		CREATE TRIGGER updateCount AFTER INSERT ON contains FOR EACH ROW
		BEGIN
			UPDATE playlist
			SET count = (
				SELECT count(*)
				FROM contains
				WHERE pname = contains.pname
			);
		END;


		CREATE TRIGGER updateName AFTER UPDATE OF pname on playlist FOR EACH ROW
		BEGIN
			UPDATE contains
			SET pname = new.pname
			WHERE contains.pname = old.pname;
		END;

		CREATE TRIGGER deleteName AFTER DELETE ON playlist FOR EACH ROW
		BEGIN
			DELETE FROM contains
			WHERE contains.pname = old.pname;
		END;

		/* Indexes/Indices*/

		CREATE INDEX KeyIndex
		ON song (location, artist, filetype, title);

		CREATE INDEX UserIndex
		ON user (uid);

		CREATE INDEX SongIndex
		ON song(genre, track, album, bitrate);

		COMMIT;""")
		self.connect.commit()
