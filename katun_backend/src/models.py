#! /usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

__all__ = ['Song', 'StaleSong', 'User', 'Authority', 'Playlist', 'session']

engine = create_engine("mysql://katun:katun@localhost:3306/katun?charset=utf8", convert_unicode=True, echo=True)
db_session = scoped_session(sessionmaker(bind=engine))
my_metadata = MetaData(bind=engine)
Base = declarative_base()
Base.query = db_session.query_property()
Base.metadata = my_metadata
s = sessionmaker(bind=engine)
session = s()



class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(length=100), nullable=False)
    permissions = relationship('Authority', backref='authority_level', lazy='joined')

    def __init__(self, name, permissions):
        self.name = name
        self.permissions = permissions

    def __repr__(self):
        return "Username {}, permissions: {}".format(self.name, self.permissions)

class Authority(Base):
    __tablename__ = 'authority'
    id = Column(Integer, primary_key=True)
    authority = Column(String(20))
    user = Column(Integer, ForeignKey('user.id'))

    def __init__(self, authority):
        self.authority = authority


class Song(Base):
    __tablename__ = 'song'
    id = Column(Integer, primary_key=True)
    entry_time = Column(DateTime, nullable=False)
    file_path = Column(String(length=2048))
    file_name = Column(String(length=1024))
    filetype = Column(String(length=4))

    def __init__(self, entry_time, file_path, file_name, filetype):
        self.entry_time = entry_time
        self.file_path = file_path
        self.file_name = file_name
        self.filetype = filetype


class Playlist(Base):
    __tablename__ = 'playlist'
    id = Column(Integer, primary_key=True)
    playlist_name = Column(String(length=255), nullable=False)
    song_id = Column(Integer, ForeignKey('song.id'), nullable=False)
    last_played_song = Column(Integer, ForeignKey('playlist.song_id'))

    def __init__(self, playlist_name, song_id):
        self.playlist_name = playlist_name
        self.song_id = song_id


class StaleSong(Base):
    __tablename__ = 'stale_song'
    id = Column(Integer, primary_key=True)
    last_update_time = Column(DateTime)
    old_location = Column(String(length=2048))

    def __init__(self, last_update, old_location):
        self.last_update_time = last_update
        self.old_location = old_location
