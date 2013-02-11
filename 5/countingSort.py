#! /usr/bin/env python
# -*- coding: utf8 -*- 
import unittest
import random

def countingSort(A,start,end):
    C = [0] * (end-start+1)
    for each in A:
        C[each-start] += 1
    C1 = [0] * (end-start+1)
    C1[0] = C[0]
    for i in range(1,len(C)):
        C1[i] = C1[i-1] + C[i]
    B = [0] * len(A)
    for each in A[::-1]:
        B[C1[each-start]-start] = each
        C1[each-start] -= 1
    return B

class Test(unittest.TestCase):
    def test1(self):
        A = [4,1,3,4,3]
        B = countingSort(A,1,4)
        A.sort()
        self.assertEqual(B,A)

    def test(self):
        for i in range(10):
            # for 10 test case
            A = []
            A_len = random.randint(1,1000)
            start = 1
            end = 100
            for a in range(0,A_len):
                A.append(random.randint(start,end))
            B = countingSort(A,start,end)
            A.sort()
            self.assertEqual(B,A)

if __name__ == '__main__':
    unittest.main()
