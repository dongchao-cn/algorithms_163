#! /usr/bin/env python
# -*- coding: utf8 -*- 
import unittest
import random

def mergeSort(l):
    if len(l) == 1:
        return l
    else:
        l1 = l[:int(len(l)/2)]
        l2 = l[int(len(l)/2):]
        l1 = mergeSort(l1)
        l2 = mergeSort(l2)
        tpl = []
        while l1 and l2:
            minele = min(l1[0],l2[0])
            tpl.append(minele)
            if l1[0] == minele:
                del l1[0]
            else:
                del l2[0]
        if l1:
            tpl += l1
        if l2:
            tpl += l2
        return tpl

class Test(unittest.TestCase):
    def test(self):
        for i in range(10):
            # for 10 test case
            l = []
            j_len = random.randint(1,1000)
            for j in range(0,j_len):
                l.append(random.randint(1,10000))
            mergel = mergeSort(l)
            l.sort()
            self.assertEqual(mergel,l)

if __name__ == '__main__':
     unittest.main()
