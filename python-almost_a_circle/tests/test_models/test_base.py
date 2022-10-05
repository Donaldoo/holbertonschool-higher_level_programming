#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test class for Base class"""
    def test_if_id_none(self):
        """test if id is none"""
        base1 = Base()
        self.assertEqual(1, base1.id)

    def test_id(self):
        """test if id is not none"""
        base1 = Base(89)
        self.assertEqual(89, base1.id)

    def test_id_negative(self):
        """test if id is negative"""
        base1 = Base(-89)
        self.assertEqual(-89, base1.id)

    def test_id_string(self):
        """test if id is string"""
        base1 = Base("id")
        self.assertEqual("id", base1.id)

    def test_id_zero(self):
        """test if id is 0"""
        base1 = Base(0)
        self.assertEqual(0, base1.id)

    def test_to_json_none(self):
        """test method to json none"""
        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, "[]")
