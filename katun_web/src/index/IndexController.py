#! /usr/bin/env python
# -*- coding: utf-8 -*-
# K'atun Index controller
# Written by Jason Black

import cherrypy

class IndexController:
    def __init__(self):
        pass

    @cherrypy.expose
    def index(self):
        return "Hello world!\nWill need to add a template engine later."

def main():
    cherrypy.quickstart(IndexController())

if __name__ == '__main__':
    main()
