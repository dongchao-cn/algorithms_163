#! /usr/bin/env python
# -*- coding: utf8 -*- 
import unittest
import random

def partition(A,p,q):
    # randomized
    randpos = random.randint(p,q)
    A[p], A[randpos] = A[randpos], A[p]

    x = A[p]
    i = p
    j = p + 1
    while j <= q:
        if A[j] >= x:
            j += 1
        else:
            A[j], A[i+1] = A[i+1], A[j]
            i += 1
            j += 1
    A[i], A[p] = A[p], A[i]
    return i

def randSelect(A,p,q,i):
    if p == q:
        return A[p]
    r = partition(A,p,q)
    k = r-p+1
    if k == i:
        return A[r]
    elif k < i:
        return randSelect(A,r+1,q,i-k)
    else:
        return randSelect(A,p,r-1,i)

class Test(unittest.TestCase):
    def test1(self):
        A = [6,10,13,5,8,3,2,11]
        i = 7
        self.assertEqual(11,randSelect(A,0,len(A)-1,i))

    def test(self):
        for i in range(10):
            # for 10 test case
            l = []
            j_len = random.randint(1, 1000)
            for j in range(0, j_len):
                l.append(random.randint(1, 10000))
            middle = randSelect(l, 0, len(l)-1, j_len/2)
            l.sort()
            self.assertEqual(middle, l[j_len/2 - 1])

if __name__ == '__main__':
    unittest.main()
