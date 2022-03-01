# This method sort's data structures as lists,tuples,dictionary and more..
# including special data structures which contains more data structures in them
# this method uses recursion we pass through all the data structures until we get to a primitive variable
def print_sorted(x):
    if isinstance(x, dict): # first we check the complected case which is a dictionary
        print ('{' ,end=' ')
        for k,v in sorted(x.items()): # sort all the keys
            print(k+' :',end=' ')
            print_sorted(v)
        print('}', end=' ')
    elif isinstance(x, list) or isinstance(x, tuple) or isinstance(x, set):
        print('[' , end=' ')
        for i in sorted(x,key=lambda x: str(x)): # we cast to string so we can compare between variables and sort

            print_sorted(i)
        print(']', end=' ')
    else:
        print(x,end=' ') # the stop condition

    return ''
###### some special cases checking#######
if __name__ == '__main__':
    x = {"a": 5, "c": {"z": 1, "y": {"apple": 2, "banana": 3}}, "b": {1, 3, 2, 4}, "e": [3, 24, 1]}
    y = [3, 1, [3, 6, 1, [1, 3, 2]], 0, {"a": {"b": 21}}]
    z={1,2,3,4}
    w=[[1],[2],3,1,[5],[4,1,3]]
    print(print_sorted(x))
    print(print_sorted(y))
    print(print_sorted(z))
    print(print_sorted(w))


