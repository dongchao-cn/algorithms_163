#! /usr/bin/env python
# -*- coding: utf8 -*- 
import unittest
import random

def insertSort(l):
    tpl = l
    for i in range(1,len(tpl)):
        tp = tpl[i]
        for j in range(i-1,-1,-1):
            if tpl[j]>tp:
                tpl[j+1] = tpl[j]
            else:
                tpl[j+1] = tp
                break
        else:
            if j == 0:
                tpl[0] = tp
    return tpl

class Test(unittest.TestCase):
    def test(self):
        for i in range(10):
            # for 10 test case
            l = []
            j_len = random.randint(1,1000)
            for j in range(0,j_len):
                l.append(random.randint(1,10000))
            insertl = insertSort(l)
            l.sort()
            self.assertEqual(insertl,l)

if __name__ == '__main__':
    unittest.main()
