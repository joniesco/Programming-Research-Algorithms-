#Question 1
#In this function we will make sure the input matching the annotaions by using annotations function and *args


def safe_call(f, *args):

    types_f = f.__annotations__.values()    # executing the values of the annotations of f so we can compare with the types of *args - the input
    types_args = [ type(x) for x in args ][0:len(types_f)]

    # print(list(types_f))
    # print(types_args)

    if list(types_f) != types_args: # it means that the input was not as required
        raise Exception("bad annotations")

    return(f(*args))





######################### ########             some examples and test cases #################################################
if __name__ == '__main__':
#--------- definning some functions with annotations-------------
    def f(x: float, y: float, z):
        return x + y + z
    def g(x: float, y: float, z:int):
        return x + y + z
    def k(x:list):
        return x
    def p(p:dict):
        return p
    def l(c:float,a,b):
        return a+b-c

    def s(c: str, a:str, b:str):
        return a + b + c
    ##good cases
    print(safe_call(f, 1.0, 2.0, 3.9))
    print(safe_call(g,1.0,2.0,3))
    print(safe_call(k,[1,2,3]))
    print(safe_call(p,{"a":12}))
    print(safe_call(l,1.0,1,2))
    print(safe_call(s, "a","a","a"))  # should throw exception


    #bad cases
    print(safe_call(f,1,2,3)) # should throw exception
    print(safe_call(f, 1, 2))  # should throw exception
    print(safe_call(p, []))  # should throw exception
    print(safe_call(k, {1,2,3}))  # should throw exception
    print(safe_call(g, 1.0,1.0,1.0))  # should throw exception
    print(safe_call(l, "a","a","a"))  # should throw exception
    print(safe_call(s, 1,2,3))  # should throw exception
