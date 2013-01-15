#! /usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from unittest.case import TestCase

from db_backend import DatabaseInterface

class TestDatabaseInterface(TestCase):

    def setUp(self):
        self.interface = DatabaseInterface()

    def tearDown(self):
        self.interface.close()

    def testOpenDbConnection(self):
        #given

        #when


        #then
        self.assertIsNotNone(self.interface.connection)
        self.assertIsNotNone(self.interface.db)

if __name__ == '__main__':
    unittest.main()

