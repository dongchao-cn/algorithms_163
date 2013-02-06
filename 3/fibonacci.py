#! /usr/bin/env python
# -*- coding: utf8 -*- 
import unittest
import random

def fib1(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib1(n-1) + fib2(n-2)

def fib2(n):
    l = [0,1]
    for i in range(2,n+1):
        l.append(l[i-1]+l[i-2])
    return l[n]

class Test(unittest.TestCase):
    def test(self):
        
        self.assertEqual(fib1(100),fib2(100))

if __name__ == '__main__':
    import profile
    profile.run("unittest.main()")
