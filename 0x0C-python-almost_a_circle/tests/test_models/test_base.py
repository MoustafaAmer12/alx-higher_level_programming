#!/usr/bin/python3
"""
Module that tests Base Class
"""
import unittest
from models import base
Base = base.Base


class TestBase(unittest.TestCase):
    """A Class that tests Base Class
    """
    @classmethod
    def setUpClass(cls):
        cls.test_a = Base()
        cls.test_b = Base(12)
        cls.test_c = Base()
    
    @classmethod
    def tearDownClass(cls):
        del cls.test_a
        del cls.test_b
        del cls.test_c

    def test_base_custom_id(self):
        self.assertEqual(self.test_b.id, 12)
        self.assertFalse(self.test_a.id == None)

    def test_counter_id(self):
        self.assertEqual(self.test_a.id, 1)
        self.assertEqual(self.test_c.id, 2)

    def test_id_not_repeated(self):
        self.test_d = Base()
        self.assertFalse(self.test_a.id == self.test_b.id)
        self.assertFalse(self.test_a.id == self.test_d.id)
        self.assertFalse(self.test_b.id == self.test_d.id)
