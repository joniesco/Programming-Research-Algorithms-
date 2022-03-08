""""a decoretor which checks whether the current input is the same as the previous input.
If so, he writes an appropriate message. If not, he he runs the function as usual
@:param mem : our global variable to remember the last call"""



mem = None


def lastcall(func):

        def inner(arg): # inner class
           global mem   # reference to our global variable
           temp = mem
           mem = arg
           if temp == mem :  # means the call is the same call as previous
               return "I already told you that the answer is " + str(func(arg))
           else:
               temp = mem
               return func(mem)


        return inner

##################### Let's check on some functions #########3



#######func1
@lastcall
def f(x: int):
    return x**2
print(f(2))
print(f(2))
print(f(3))
print(f(2))
print(f(3))
print(f(3))
print(f(3))

#######func2
@lastcall
def f(x: int):
    return x**2 -x +3      ## here f(0)=f(1) but still it returns 3 ,3 after calling f(0) and then f(1)
print(f(0))
print(f(0))
print(f(0))
print(f(1))
print(f(0))
print(f(1))
#######func3
@lastcall
def f(x: int):
    return 0
print(f(0))      ## here f(x)=0 for every x but still works fine
print(f(0))
print(f(2))
print(f(2))
print(f(0))