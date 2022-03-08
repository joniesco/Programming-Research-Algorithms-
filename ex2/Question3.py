import unittest
from unittest import TestCase
""" This class is Same as Python list but allows items to be accessed in multidimensional array syntax
for using the normal list method put self.l"""
class List():
    # Constructor l is our list
    def __init__(self, l:list):
        self.l = l

    def __str__(self):
        # To string
        return str(self.l)

    def __getitem__(self, item):
        #overloading the operator [] so we can print can give access to multidimensional array syntax


        if isinstance(item,int):  # case of normal list
            return self.l[item]

        arr = self.l  # arr will represent the depth we want to get
        for i in item:
            arr = arr[i]  # updating arr depending the depth

        return arr

    def __setitem__(self, key, value):
        if isinstance(key, int):  # case of normal list
             self.l.__setitem__(key,value)



class TestFindRoot(TestCase):

    def test_List(self):
        mylist1 = List([
            [[1, 2, 3, 33], [4, 5, 6, ['a', 'b', 'c']]],
            [[7, 8, 9, 99], [10, 11, 12, 122]],
            [[13, 14, 15, 155], [16, 17, 18, 188]]
        ])
        mylist2 = List([1,2,4])

        mylist3 = List([1,3,2,[8,1,2,[0,[3]]]])

        self.assertEqual('b',mylist1[0,1,3,1])
        self.assertEqual(mylist2[0],1)
        self.assertEqual(mylist2[0],mylist1[0,0,0])
        self.assertEqual(3,mylist3[3,3,1,0])
        mylist2.l.append(3)                  # works like normal list
        self.assertEqual(mylist2[3],3)
        mylist3.l.remove(1)
        self.assertEqual(3,mylist3[0])
        mylist2[0,1,2]=3
        mylist3[0]=6                    #operator [] works
        self.assertEqual(6,mylist3[0])




if __name__ == '__main__':
    unittest.main()
