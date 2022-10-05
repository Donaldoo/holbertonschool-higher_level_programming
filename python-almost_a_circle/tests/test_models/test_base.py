#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_if_id_none(self):
    """test if id is none"""
        base1 = Base()
        self.assertEqual(1, b.id)
