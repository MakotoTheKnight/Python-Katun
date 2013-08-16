#! /usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from unittest.case import TestCase

from database import BackendDatabaseInterface


class TestDatabaseInterface(TestCase):

    def setUp(self):
        self.interface = BackendDatabaseInterface()

    def tearDown(self):
        self.interface.close()

    def testOpenDbConnection(self):
        #given

        #when

        #then
        self.assertIsNotNone(self.interface.conn)

if __name__ == '__main__':
    unittest.main()

