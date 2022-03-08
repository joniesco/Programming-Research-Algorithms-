# this function using the Newton–Raphson method which produces successively better approximations to the roots (or zeroes) of a real-valued function
#as described in
# https://he.wikipedia.org/wiki/%D7%A9%D7%99%D7%98%D7%AA_%D7%A0%D7%99%D7%95%D7%98%D7%95%D7%9F-%D7%A8%D7%A4%D7%A1%D7%95%D7%9F
import unittest
from unittest import TestCase
def find_root(f,a,b):
    eps = 0.00001 # defining a very small number which will help us to know we are close enough to the root
    x_n = (a+b)/2 # choosing a random number on the interval in this case the average of a and b

    x_n1=0  ## x_n1 intizilized to 0 for the case f(x)= 0 so we will just return 0

    while abs(f(x_n1)) > eps: ## when the loop ends it means we are close enough to the root
        if(f_tag(f,x_n))==0:  ## for cases like f(x)=0 and for not dividing by zero
            break
        x_n1 = x_n - f(x_n) / f_tag(f,x_n)
        x_n = x_n1
    return x_n1

# method to derivative a function using definition
def f_tag (f,x):
    h=0.0000001
    return (f(x+h)-f(x))/h
if __name__ == '__main__':
    ## some function examples

    print(find_root(lambda x: x ** 3 - 5 * x - 9, 1, 3)) # should print ~2.9
    print(find_root(lambda x: x ** 2 - 4, 1, 3)) #should print ~2.0
    print(find_root(lambda x: x ** 3 , 0, 2))  # should print ~0.1
    print(find_root(lambda x: x ** 5-6*x**2+x-10, 0, 2))  # should print ~2.0
    print(find_root(lambda x: x**2-1, 2, 10))  # should print ~1.0
    print(find_root(lambda x: 0, 2, 10))# should print 0
    print(find_root(lambda x: x ** 2 - 4, -3, -1))# should print ~-2.0
    print(find_root(lambda x: x ** 2 - 4, -1, 1))# should print ~2.0
    print(find_root(lambda x: x ** 2 - 16, 3, 5))  # should print ~4.0
    print(find_root(lambda x: x ** x - 2, 3, 5))  # should print ~1.55


    class TestFindRoot(TestCase):
        def test_find_root(self):
            self.assertTrue(-2.1 <= find_root(lambda x: x ** 2 - 4, -3, -1) <= -1.9)# should print ~ -2.0
            self.assertTrue(2.8 <= find_root(lambda x: x ** 3 - 5 * x - 9, 1, 3) <= 3) # should print ~2.9
            self.assertTrue(1.99 <= find_root(lambda x: x ** 2 - 4, 1, 3) <= 2.1)#should print ~2.0
            self.assertTrue(0 <= find_root(lambda x: x ** 3 , 0, 2) <= 0.2) # should print ~0.1
            self.assertTrue(1.9 <= find_root(lambda x: x ** 5-6*x**2+x-10, 0, 2) <= 2.1)# should print ~2.0
            self.assertTrue(0.99 <= find_root(lambda x: x**2-1, 2, 10) <= 1.1)# should print ~1.0
            self.assertTrue(4.000 <= find_root(lambda x: x ** 2 - 16, 3, 5) <= 4.1)  # should print ~4.0
            self.assertTrue(1.54 <= find_root(lambda x: x ** x - 2, 1, 5) <= 1.56)  # should print ~1.55

                ### cases of 0 ###
            self.assertEqual(find_root(lambda x: 0, 2, 10),0)
            self.assertEqual(find_root(lambda x: x, 0, 0), 0)
            self.assertEqual(find_root(lambda x: x, 3, 3), 0)
            self.assertEqual(find_root(lambda x: x**8, 3, 3), 0)


            self.assertEqual(find_root(lambda x: 2, 2, 10), 0)


    if __name__ == '__main__':
        unittest.main()