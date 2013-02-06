#! /usr/bin/env python
# -*- coding: utf8 -*- 
import unittest
import random

def binarySearch(l,ele):
    if len(l) == 0:
        return None
    if ele == l[len(l)/2]:
        return len(l)/2
    elif ele > l[len(l)/2]:
        return binarySearch(l[len(l)/2+1:],ele)
    else:
        return binarySearch(l[:len(l)/2],ele)

class Test(unittest.TestCase):
    def test1(self):
        l = range(1,10)
        ele = 3
        pos = binarySearch(l,ele)
        self.assertEqual(pos,l.index(ele))

    def test2(self):
        l = range(2,10)
        ele = 1
        pos = binarySearch(l,ele)
        self.assertEqual(pos,None)
        
    def test3(self):
        l = range(2,10)
        ele = 11
        pos = binarySearch(l,ele)
        self.assertEqual(pos,None)
        
    def test4(self):
        l = range(5,10) + range(15,20)
        ele = 12
        pos = binarySearch(l,ele)
        self.assertEqual(pos,None)

if __name__ == '__main__':
    unittest.main()
