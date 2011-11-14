#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Katun MP3/Ogg Vorbis Parser
# This library is designated to parse the files from a user's library.

import mutagen, os, sqlite3, exceptions, time

#path = raw_input("Insert the full path of the songs you want to parse. >\t")

class InvalidSongException(Exception): pass

class Parser:
	'''Parse an entire directory of files in order to gain the tags.
	Per the specifications, we will only be paying attention to the following tags:
	location, artist, filetype, title, genre, track, album, bitrate, year, and month.
	Only location, artist, filetype, and title must be non-empty.'''
	
	def __init__(self, path, db_path="../../db/Katun.db"):
		'''Accept a path to the music directory and (optionally) the database.'''
		self.path, self.db_path = path, db_path
		self.connect = sqlite3.connect(db_path)
		self.cursor = self.connect.cursor()
		start = time.time()
		self.walk(path)
		stop = time.time()
		print "SPAMMING TOOK " + str(stop - start) + " seconds."
	
	def walk(self, d):
		'''Begin walking down the file structure recursively, gathering the UTF-8 file names to read in.
		Source:  ssscripting.wordpress.com/2009/03/03/python-recursive-directory-walker'''
		d = os.path.abspath(d)
		for f in [f for f in os.listdir(d) if not f in [".",".."]]:
			nfile = os.path.join(d, f)
			if os.path.isfile(nfile):
				try:
					self.parse(nfile)
				except InvalidSongException, e:
					print nfile + ' ' + str(e)
			if os.path.isdir(nfile):
				self.walk(nfile)
	
	def parse(self, filename):
		'''Parse the file into the appropriate information we want.'''
		filename = filename.decode('utf-8')
		song = mutagen.File(filename, easy=True)
		artist, title, genre, track, album, bitrate, year, month = '', '', '', '', '', '', '', ''
		try:
			artist = song['artist'][0]
			title = song['title'][0]
		except Exception:
			raise InvalidSongException("Song doesn't have an artist or title, so will not be added into database.")
		if 'genre' in song:
			genre = song['genre'][0]
		else:
			genre = u'Unknown'
		if 'tracknumber' in song:
			track = song['tracknumber'][0]
		else:
			track = 0
		if 'album' in song:
			album = song['album'][0]
		else:
			album = u'Unknown'
		if 'year' in song:
			year = int(song['year'][0])
		else:
			year = 0
		if 'month' in song:
			month = int(song['month'][0])
		else:
			month = 0
		try:
			bitrate = int(song.info.bitrate)
		except AttributeError: # Likely due to us messing with FLAC
			bitrate = 999999 # Set to a special flag value, to indicate that this is a lossless file.
		
		attributes = filename, artist, filename.split('.')[-1], title, genre, track, album, bitrate, year, month
		try:
			self.cursor.execute("INSERT INTO song VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", attributes)
			self.connect.commit()
		except Exception, e:
			pass
		except InvalidSongException, e:
			print "Song " + filename + " couldn't  be read.  Reason: " + e
		

def main():
	parser = Parser(raw_input("Enter the path of the music. > "))
	
if __name__ == '__main__':
	main()
