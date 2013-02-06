#! /usr/bin/env python
# -*- coding: utf-8 -*-
from mongoengine import *

__all__ = ['BackendDatabaseInterface', 'DatabaseError']

__metaclass__ = type


class DatabaseError(Exception): pass


class BackendDatabaseInterface(object):

    def __init__(self):
        self.conn = connect('katun_backend', 'katun_db')

    def close(self):
        self.conn.disconnect()


