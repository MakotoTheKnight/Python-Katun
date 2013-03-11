#! /usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
import os

from db_backend import Song, db

__all__ = ['walk', 'parse']

supported = ['.ogg', '.flac', '.mp3']


def load_directory(d):
    absolute_path = os.path.abspath(d)
    for path, foldernames, files in os.walk(absolute_path):
        for f in files:
            extension = os.path.splitext(f)
            if extension[1] in supported:
                load_song_in_db(os.path.join(path, f), extension)
            else:
                print "File not supported at this time, {}".format(f)


def load_song_in_db(filename, ext):
    try:
        db.session.add(Song(datetime.today().isoformat(), filename, ext[-1].replace('.', '')))
        db.session.commit()
    except Exception as e:
        print "WHAT THE HECK WENT WRONG.", e


def main():
    load_directory(raw_input(u"Enter the path of the music. > "))

if __name__ == '__main__':
    main()
