#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://katun:katun@localhost:3306/katun?charset=utf8"
db = SQLAlchemy(app)


class DatabaseError(Exception):
    pass


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=100))
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
    entry_time = db.Column(db.DateTime)
    file_location = db.Column(db.String(length=2048))

    def __init__(self, entry_time, file_location):
        self.entry_time = entry_time
        self.file_location = file_location

    def __str__(self):
        return "Entry time={}, location={}"


class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=255), unique=True)
    dynamic = db.Column(db.Boolean)
    size = db.Column(db.Integer)

    def __init__(self, name, dynamic, size):
        self.name = name
        self.dynamic = dynamic
        self.size = size


class StaleSong(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    last_update_time = db.Column(db.DateTime)
    old_location = db.Column(db.String(length=2048))

    def __init__(self, last_update, old_location):
        self.last_update_time = last_update
        self.old_location = old_location


class BackendDatabaseInterface(object):
    # Should be the only thing exposed; no need to use the model/table objects directly.

    def __init__(self, db_type):
        pass


def main():
    db.create_all()

if __name__ == '__main__':
    main()