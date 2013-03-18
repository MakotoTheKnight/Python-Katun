#! /usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

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


# Base = declarative_base()
# db_session = scoped_session(sessionmaker(bind=engine))
# my_metadata = MetaData(bind=engine)
# Base.query = db_session.query_property()
# Base.metadata = my_metadata
# s = sessionmaker(bind=engine)
# session = s()