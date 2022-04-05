"""
In this question we write an  generator named subsets_bounded. It receives as input S a group of positive numbers, and numbers
Positive C, and produces a series of all subsets of S, the sum of which is at most C. The solution should be as efficient as possible.
Based on https://www.geeksforgeeks.org/print-sums-subsets-given-set/
will work fine with this solution because we get only positive numbers but we need to sort the given list
"""
import unittest
from unittest import TestCase
import random
def bounded_subsets(arr, C):
    # There are total 2^n subsets
    arr = sorted(arr)
    n = len(arr)
    total = 2**n
    # Consider all numbers from 0 to 2^n - 1
    for i in range(total):
        Sum = 0
        sub_arr = []
        # Consider binary representation of
        # current i to decide which elements
        # to pick.
        for j in range(n):
            if ((i & (1 << j)) != 0):
                Sum += arr[j]
                sub_arr.append(arr[j])
                if Sum > C:
                    break
        if Sum > C:
            break
        yield sub_arr ## we yield just when sum<c
class TestFindRoot(TestCase):

    def test_List(self):
        list = []
        list1_test = []
        list2_test = []
        list3_test = []


        for i in range(1,10):
            list.append(i)
        arr = [1, 2, 3]

        for s in bounded_subsets(list, 1):
            list1_test.append(s)
        for s in bounded_subsets(list, 5):
            list2_test.append(s)
        for s in bounded_subsets(arr, 4):
            list3_test.append(s)
        self.assertEqual(list1_test,[[], [1]])
        self.assertEqual(list2_test,[[], [1], [2], [1, 2], [3], [1, 3], [2, 3]])
        self.assertEqual(list3_test,[[], [1], [2], [1, 2], [3], [1, 3]])

        ## Let's make a random list of numbers 1-100 with length 5

        res = [random.randrange(1, 100, 1) for i in range(5)]
        print(res)
        res_t=[]
        for s in bounded_subsets((res), 40):
            res_t.append(s)
        print(res_t)
            ## works Ok

