#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

__all__ = ['User', 'Authority', 'Song', 'StaleSong', 'Playlist', 'db']

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://katun:katun@localhost:3306/katun?charset=utf8"
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=100), nullable=False)
    permissions = db.relationship('Authority', backref='authority_level', lazy='joined')

    def __init__(self, name, permissions):
        self.name = name
        self.permissions = permissions

    def __str__(self):
        return "Username {}, permissions: {}".format(self.name, self.permissions)


class Authority(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    authority = db.Column(db.String(20))
    user = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, authority):
        self.authority = authority


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entry_time = db.Column(db.DateTime, nullable=False)
    file_location = db.Column(db.String(length=2048))
    filetype = db.Column(db.String(length=4))

    def __init__(self, entry_time, file_location, filetype):
        self.entry_time = entry_time
        self.file_location = file_location
        self.filetype = filetype

    def __str__(self):
        return "Entry time={}, location={}"


class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    playlist_name = db.Column(db.String(length=255), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey('song.id'), nullable=False)
    last_played_song = db.Column(db.Integer, db.ForeignKey('playlist.song_id'))

    def __init__(self, playlist_name, song_id):
        self.playlist_name = playlist_name
        self.song_id = song_id


class StaleSong(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    last_update_time = db.Column(db.DateTime)
    old_location = db.Column(db.String(length=2048))

    def __init__(self, last_update, old_location):
        self.last_update_time = last_update
        self.old_location = old_location


db.create_all()
