#! /usr/bin/env python
# -*- coding: utf-8 -*-

import mutagen, os, time
from db_backend import BackendDatabaseInterface

__all__ = ['walk', 'parse']

def walk(self, d):
    d = os.path.abspath(d)
    dirpath = os.walk(d)
    for folder in dirpath:
        for f in folder[2]: # for each file in the folder...
            supported = 'mp3', 'ogg', 'flac'
            if f.split('.')[-1] in supported:
                try:
                    self.parse(os.path.join(folder[0], f))
                except Exception, e:
                    print e.__unicode__()
    try:
        self.db.execute_batch_insert_statement(u"INSERT INTO song VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", self.buf)
    except Exception, e:
        print e.__unicode__()
    finally:
        del self.buf
        self.buf = []


def parse(self, filename):
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
    self.buf.append((filename, artist, filename.split('.')[-1], title, genre, track, album, bitrate, year, time.time()))


def main():
        '''main() functions are used to test the validity and performance of the module alone.
         This function is to NEVER be called outside of testing purposes.'''
        parser = Parser(raw_input(u"Enter the path of the music. > "), startfresh=True)

if __name__ == '__main__':
    main()
