#! /usr/bin/env python
# -*- coding: utf8 -*- 
import unittest
import random

def matrix1(m,n):
    x = []
    for i in range(len(m)):
        x.append([])
        for j in range(len(n[0])):
            x[i].append(0)
            for k in range(len(m[i])):
                x[i][j] += m[i][k] * n[k][j]
    return x

class Test(unittest.TestCase):
    def test(self):
        
        m = [
        [1,2,3,2],
        [4,5,6,4],
        [7,8,9,3],]

        n = [
        [3,4,5],
        [1,2,3],
        [6,7,8],
        [7,8,9],
        ]

        x = [
        [37,45,53],
        [81,100,119],
        [104,131,158],
        ]
        self.assertEqual(matrix1(m,n),x)

if __name__ == '__main__':
    unittest.main()
