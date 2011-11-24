#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Katun MP3/Ogg Vorbis Parser
# This library is designated to parse the files from a user's library.

import lib.mutagen as mutagen, os, sqlite3, exceptions, time


class InvalidSongException(Exception): pass

class Parser:
	'''Parse an entire directory of files in order to gain the tags.
	Per the specifications, we will only be paying attention to the following tags:
	location, artist, filetype, title, genre, track, album, bitrate, year, and month.
	
	Location, Artist, Filetype, and Title are keys, and must be non-empty.  We can retrieve
	the location and filetype of the song trivially; however, if artist and title do not exist, then we
	cannot parse the song.'''
	
	def __init__(self, path, db_path="../db/Katun.db"):
		'''Accept a path to the music directory and (optionally) the database.
		Unless otherwise specified in another document, the database should exist in the ../db folder.'''
		self.path, self.db_path = path, db_path
		self.connect = sqlite3.connect(db_path)
		self.cursor = self.connect.cursor()
		self.filecount, self.attempted = 0, 0
		
		start = time.time()
		self.walk(path)
		stop = time.time()
		print u"Elapsed time: " + str(stop-start) + "\nTotal files entered: " + str(self.filecount) + "\nAttempted: " + str(self.attempted)
	
	def walk(self, d):
		'''Walk down the file structure iteratively, gathering file names to be read in.'''
		d = os.path.abspath(d)
		generator = os.walk(d)
		for folder in generator:
			for f in folder[2]: # foreach file in the folder...
				try:
					supported = 'mp3', 'ogg', 'flac'
					if f.split('.')[-1] in supported:
						self.parse(unicode(os.path.join(folder[0], f), 'utf_8'))
					else:
						print u"Not going to bother with file " + unicode(os.path.join(folder[0], f), 'utf_8')
				except Exception, e:
					print e.__unicode__()
	
	def parse(self, filename):
		'''Parse the file to retrieve the information we want.
		
		It may be the case that, in the future, we require more information from a song than is provided at this time.
		Examine all tags that can be retrieved from a mutagen.File object.'''
		
		self.attempted += 1
		song = mutagen.File(filename, easy=True)
		artist, title, genre, track, album, bitrate, year, month = '', '', '', '', '', '', '', ''
		try:
			artist = song['artist'][0]
			title = song['title'][0]
		except Exception:
			raise InvalidSongException(u"Cannot read " + filename + ": missing critical song information.")
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
		if 'date' in song:
			year = song['date'][0]
		else:
			year = 'Unknown'
		try:
			bitrate = int(song.info.bitrate)
		except AttributeError: # Likely due to us messing with FLAC
			bitrate = 999999 # Set to a special flag value, to indicate that this is a lossless file.
		try:
			attributes = filename, artist, filename.split('.')[-1], title, genre, track, album, bitrate, year, time.time()
			self.cursor.execute(u"INSERT INTO song VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", attributes)
			self.connect.commit()
			self.filecount += 1
		except Exception, e:
			raise InvalidSongException(filename + u" was not inserted into database - " + str(e))


def main():
	'''main() functions are used to test the validity and performance of the module alone.
	This function is to NEVER be called outside of testing purposes.'''
	parser = Parser(raw_input(u"Enter the path of the music. > "))
	
if __name__ == '__main__':
	main()
