#! /usr/bin/env python
# -*- coding: utf8 -*- 
import unittest
import random

def poweringN(x,n):
    if n == 1:
        return x
    if n % 2 == 0:
        return poweringN(x,n/2)**2
    else:
        return poweringN(x,n/2)**2 * x

class Test(unittest.TestCase):
    def test(self):
        x = 3.0
        ns = [2,3,100,101]
        for n in ns:
            self.assertEqual(poweringN(x,n),x**n)

if __name__ == '__main__':
    unittest.main()
