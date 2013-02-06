#! /usr/bin/env python
# -*- coding: utf-8 -*-

from mongoengine import *


class Katun_User(Document):
    username = StringField(required=True, max_length=50)


class Playlist(Document):
    name = StringField(required=True)
    size = IntField(min_value=1)
    metadata = PlaylistMetadata()


class DynamicPlaylist(Playlist):
    pass


class Song(Document):
    pass


class VorbisSong(Song):
    pass


class MP3Song(Song):
    pass


class FLACSong(Song):
    pass


class SongMetadata(EmbeddedDocument):
    pass


class PlaylistMetadata(EmbeddedDocument):
    is_dynamic = BooleanField(validation=True)

