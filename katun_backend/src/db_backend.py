#! /usr/bin/env python
# -*- coding: utf-8 -*-
from pymongo.errors import ConnectionFailure
from pymongo.mongo_client import MongoClient

__all__ = ['DatabaseInterface', 'DatabaseError']

import pymongo

__metaclass__ = type

class DatabaseError(Exception): pass


class DatabaseInterface(object):

    def __init__(self):
        self.db = None
        try:
            self.connection = MongoClient()
            self.db = self.connection['katun']
        except ConnectionFailure as cf:
            print("Couldn't start Mongo - make sure that the daemon is running properly. Stack:\n" + cf.__str__())
            self.connection = None

    def close(self):
        self.connection.disconnect()


