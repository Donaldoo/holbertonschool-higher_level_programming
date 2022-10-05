#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_if_id_none(self):
    """test if id is none"""
        base1 = Base()
        self.assertEqual(1, base1.id)

    def test_id(self):
        """test if id is not none"""
        base1 = Base(89)
        self.asserEqual(89, base1.id)
