import numpy as np

aTest = [[0, 6, 4, 2, 0, 5, 7, 1, 3], [2, 2, 4, 6, 0, 5, 7, 1, 1], [2, 2, 4, 6, 0, 5, 7, 1, 1], [2, 2, 4, 6, 0, 5, 1, 1, 7], [5, 2, 0, 2, 0, 5, 1, 1, 7], [5, 6, 4, 
2, 4, 5, 7, 1, 1]]

def removeA(x):
    for i in range(len(x)):
        if i+1<len(x) and np.array_equal(x[i],x[i+1]):
            print("dup", x[i+1])
            
    print(x)
def sets(x):
    tmp = set()
    newA = []
    for i in x:
        tmp.add(tuple(i))
    s=list(tmp)
    print(s)

sets(aTest)
#removeA(aTest)