#! /usr/bin/env python
# -*- coding: utf8 -*- 
import unittest
import random

def insertSort(l):
    for i in range(1,len(l)):
        tp = l[i]
        for j in range(i-1,-1,-1):
            if l[j]>tp:
                l[j+1] = l[j]
            else:
                l[j+1] = tp
                break
        else:
            if j == 0:
                l[0] = tp
    return l

class Test(unittest.TestCase):
    def test(self):
        for i in range(10):
            # for 10 test case
            l = []
            j_len = random.randint(1,1000)
            for j in range(0,j_len):
                l.append(random.randint(1,10000))
            insertl = l
            insertSort(insertl)
            l.sort()
            self.assertEqual(insertl,l)

if __name__ == '__main__':
    unittest.main()
