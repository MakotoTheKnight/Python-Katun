#! /usr/bin/env python
# -*- coding: utf-8 -*-

from exceptions import NotImplementedError
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import models


__all__ = ['get_base', 'get_session']


def __get_engine(ptcl='mysql+mysqldb', usr='katun', pw='katun', svr='localhost',
               port=3306, tbl='katun'):
    return create_engine(ptcl + '://' + usr + ':' + pw + '@' + svr + ':'
                         + str(port) + '/' + tbl + '?charset=utf8',
                         echo=True)


def get_base(ptcl='mysql+mysqldb', usr='katun', pw='katun', svr='localhost',
               port=3306, tbl='katun'):
    engine = __get_engine(ptcl, usr, pw, svr, port, tbl)
    session_with_scope = scoped_session(sessionmaker(bind=engine))
    base = declarative_base()
    base.query = session_with_scope.query_property()
    base.metadata = MetaData(bind=engine)
    return base


def get_session():
    engine = __get_engine()
    return sessionmaker(bind=engine)()


class DatabaseConnection(object):
    def __init__(self, ptcl='mysql+mysqldb', usr='katun', pw='katun', svr='localhost',
               port=3306, tbl='katun'):
        self.base = get_base(ptcl, user, pw, svr, port, tbl)
        self.session = get_session()

    def add(self, model, **kwargs):
        if type(model) is not self.base:
            raise NotImplementedError('This type of model is not currently supported by Katun.')
        else:
            # TODO:  Add context-aware keyword arguments (if a model doesn't support it, don't bother)
            self.session.begin()
            self.session.add(model(kwargs))

