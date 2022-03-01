# this function using the Newton–Raphson method which produces successively better approximations to the roots (or zeroes) of a real-valued function
#as described in
# https://he.wikipedia.org/wiki/%D7%A9%D7%99%D7%98%D7%AA_%D7%A0%D7%99%D7%95%D7%98%D7%95%D7%9F-%D7%A8%D7%A4%D7%A1%D7%95%D7%9F

def find_root(f,a,b):
    eps = 0.00001 # defining a very small number which will help us to know we are close enough to the root
    x_n = (a+b)/2 # choosing a random number on the interval in this case the average of a and b
    x_n1 = x_n - f(x_n)/f_tag(f,x_n)
    # print(x_n)
    # print(x_n1)
    while abs(f(x_n1)) > eps: ## when the loop ends it means we are close enough to the root
        x_n1 = x_n - f(x_n) / f_tag(f,x_n)
        x_n = x_n1
    return x_n

# method to derivetieve a function using defenition
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