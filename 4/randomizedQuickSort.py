#! /usr/bin/env python
# -*- coding: utf8 -*- 
import unittest
import random

def partition(A,p,q):

    # randomized
    randpos = random.randint(p,q)
    tp = A[randpos]
    A[randpos] = A[p]
    A[p] = tp

    x = A[p]
    i = p
    j = p + 1
    while j <= q:
        if A[j] >= x:
            j += 1
        else:
            tp = A[j]
            A[j] = A[i+1]
            A[i+1] = tp
            i += 1
            j += 1
    tp = A[i]
    A[i] = x
    A[p] = tp
    return i

def quickSort(A,p,q):
    if p < q:
        i = partition(A,p,q)
        quickSort(A,p,i-1)
        quickSort(A,i+1,q)

class Test(unittest.TestCase):
    def test(self):
        for i in range(10):
            # for 10 test case
            l = []
            j_len = random.randint(1,1000)
            for j in range(0,j_len):
                l.append(random.randint(1,10000))
            quickl = l
            quickSort(quickl,0,len(quickl)-1)
            l.sort()
            self.assertEqual(quickl,l)

if __name__ == '__main__':
    unittest.main()
