import unittest
from ..model.model import to_uppercase
from unittest import TestCase


class ModelTest(TestCase):
    def test_uppercase(self):
        self.assertEqual(to_uppercase('abc'), 'ABC_')

if __name__ == '__main__':
    unittest.main()
