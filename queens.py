import random
import numpy as np
import matplotlib as mlt
from matplotlib import pyplot

_queenSet = [
    # [8,0,0,0,0,0,0,0,0], # 8 conflict(s)
    # [7,3,7,0,0,0,0,0,0], # 7 conflict(s)
    # [4,1,7,5,0,2,4,6,3], # 4 conflict(s)
    # [3,3,7,0,4,6,1,2,1], # 3 conflict(s)
    # [2,2,4,2,0,5,7,1,1], # 2 conflict(s)
    # [2,2,4,2,0,5,7,1,1], # 2 conflict(s)
    # [0,6,4,2,0,5,7,1,3]  # 0 conflict(s)
]



def createQueen():
    q = [0,random.randrange(0,8),random.randrange(0,8),random.randrange(0,8),
         random.randrange(0,8),random.randrange(0,8),random.randrange(0,8),random.randrange(0,8),random.randrange(0,8)]
    fitness(q)
    _queenSet.append(q)

# Checks the number of conflicts
def fitness(x):
    placement = x[slice(1,9)]
    numOfConflict = len(placement) - len(set(placement))

    #conflictFlag = []
    for i in range(len(placement)-1):
        for j in range(i+1,len(placement)):
            if abs(placement[i]-placement[j]) == abs(i-j):
                #conflictFlag.append(j)
                numOfConflict +=1

    x[0] = numOfConflict
    #print(numOfConflict)
    return numOfConflict

def mutate(x):
    #print(type(x))
    index1 = random.randint(0,7)
    index2 = random.randint(0,7)
    while index2 == index1:
        index2 = random.randint(0,7)
    #print("index:", index1, index2)
    temp = x[index1]
    x[index1] = x[index2]
    x[index2] = temp
    return x

def crossover(x,y):
    cut = random.randint(1,6)
    #print(cut)
    fit1Left = x[slice(0,cut)]
    fit1Right = x[slice(cut,8)]
    fit2Left = y[slice(0,cut)]
    fit2Right = y[slice(cut,8)]
    
    # if len(fit1Left) < len(fit2Right):
    #     print(fit1Left, fit2Right)
    #     dif = set(fit2Right)-set(fit1Left)
    #     print("dif L:",dif)
    #     print("Len: ", len(dif))
    
    # if len(fit2Right) < len(fit1Left):
    #     dif = set(fit1Left)-set(fit2Right)
    #     print("dif R:",dif)
    
    child1 = [0] + fit1Left + fit2Right
    child2 = [0] + fit2Left + fit1Right
    
    fitness(child1)
    fitness(child2)
    # print("C1:",child1)
    # print("C2:", child2)
    return [child1,child2]
    

def parentSelection(x,y):
    #print(type(x))
    fit1 = mutate(x[slice(1,9)])
    fit2 = mutate(y[slice(1,9)])
    return crossover(fit1,fit2)

def removeLeastFit(x):
    if len(x)>5:
        x.pop()
        x.pop()
    #print(x)


for i in range(100):
    createQueen()

def checkDupe(x):
    tmp = set()
    newA = []
    for i in x:
        tmp.add(tuple(i))
    s=list(tmp)
    return s

def selectMostFit(x):
    mostFit = []
    for i in range(5):
        if(len(x)<5):return
        #print(i, len(x))
        mostFit.append(x[i])
    return mostFit

_queenSet = checkDupe(_queenSet)
_queenSet = sorted(_queenSet)
#print(type(_queenSet))
# Sorts fitness based on number of conflicts
_queenFitness = selectMostFit(_queenSet)
#print(type(_queenFitness))
#print(len(_queenFitness))


i = 100000
while i > 0:
    #print("Old:", _queenFitness)
    # #print("before:",_queenSet)
    removeLeastFit(_queenSet)
    #print("after:",_queenSet)
    if(len(_queenSet)<100):createQueen()
    #print(_queenSet)
    index1 = random.randrange(0,5)
    index2 = random.randrange(0,5)
    while index2 == index1:
        index2 = random.randrange(0,5)
    #print("Selected Parents: ", _queenFitness[index1],_queenFitness[index2])
    newChildren = parentSelection(list(_queenFitness[index1]), list(_queenFitness[index2]))
    #print("chil:",newChildren)
    _queenSet += newChildren
    _queenSet = checkDupe(_queenSet)
    _queenSet = sorted(_queenSet)
    #print("New",_queenSet)
    _queenFitness = selectMostFit(_queenSet)
    #print(_queenFitness)
    #print("New:", set(_queenFitness))
    i -=1


print(sorted(_queenSet))
print(len(_queenSet))

data = [[1, 0, 1, 0, 1, 0, 1, 0],
 [0,1,0,1,0,1,0,1],
 [1, 0, 1, 0, 1, 0, 1, 0],
 [0,1,0,1,0,1,0,1],
 [1, 0, 1, 0, 1, 0, 1, 0],
 [0,1,0,1,0,1,0,1],
 [1, 0, 1, 0, 1, 0, 1, 0],
 [0,1,0,1,0,1,0,1],
 ]

def defaultData():
    global data
    data = [[1, 0, 1, 0, 1, 0, 1, 0],
 [0,1,0,1,0,1,0,1],
 [1, 0, 1, 0, 1, 0, 1, 0],
 [0,1,0,1,0,1,0,1],
 [1, 0, 1, 0, 1, 0, 1, 0],
 [0,1,0,1,0,1,0,1],
 [1, 0, 1, 0, 1, 0, 1, 0],
 [0,1,0,1,0,1,0,1],
 ]

dataSol = []

def convert(x):
    global data
    for i in range(8):
        data[x[i+1]][i] = 2
    return data

# if _queenSet[0][0]==0:
#     convert(_queenSet[0])

sol = 0
while _queenSet[i][0]==0:
    dataSol.append(convert(_queenSet[i]))
    print(dataSol[i])
    defaultData()
    sol +=1
    i+=1

print(sol)
for i in range(sol):
    pyplot.figure(figsize=(5,5),num=i)
    pyplot.imshow(dataSol[i])

pyplot.show()

