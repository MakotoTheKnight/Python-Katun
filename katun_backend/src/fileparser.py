#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import database
from datetime import datetime
from time import time
from models import Song, session

__all__ = ['walk', 'parse']

supported = ('.ogg', '.flac', '.mp3')


def load_directory(d):
    absolute_path = os.path.abspath(d)
    for path, dirnames, files in os.walk(absolute_path):
        for f in files:
            extension = os.path.splitext(f)
            if extension[1] in supported:
                load_song_in_db(path, f, extension)
            else:
                print "File not supported at this time: {}".format(f)
    start = time()
    session.commit()
    print "Took {} seconds for this commit".format(time() - start)


def load_song_in_db(filepath, filename, ext):
    try:
        session.add(Song(datetime.today().isoformat(), filepath, filename, ext[-1].replace('.', '')))
    except Exception as e:
        print "WHAT THE HECK WENT WRONG.", e


def main():
    load_directory(raw_input(u"Enter the path of the music. > "))

if __name__ == '__main__':
    main()
