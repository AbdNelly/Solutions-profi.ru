# -*- coding: utf-8 -*-
"""tests

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LPXY7gXw-r8grGsTXHXtM_IQju--yMf0
"""

pip install calc

L = [1, 3, 2, 1, 5, 3, 5, 1, 4]

import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_RemoveDuplicates(self):
        self.assertEqual(calc.RemoveDuplicates(L), [1, 3, 2, 5, 4])