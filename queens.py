import random

_queenPlacement = [
    [8,0,0,0,0,0,0,0,0], # 8 conflict(s)
    [3,3,7,0,4,6,1,1,1], # 3 conflict(s)
    [6,3,7,0,0,0,0,0,0], # 6 conflict(s)
    [2,6,4,2,0,5,7,1,1], # 2 conflict(s)
    [2,1,7,5,0,2,4,3,3]  # 2 conflict(s)
]

# Checks the number of conflicts
def fitness(x):
    placement = x[slice(1,9)]
    numOfConflict = len(placement)+1 - len(set(placement))
    # for i in placement:
    #     print(i, placement[i])

    x[0] = numOfConflict
    print(numOfConflict)
    return numOfConflict

def mutate(x):
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
    cut = random.randint(1,8)
    fit1Left = x[slice(0,cut)]
    fit1Right = x[slice(cut,8)]
    fit2Left = y[slice(0,cut)]
    fit2Right = y[slice(cut,8)]
    child1 = [0] + fit1Left + fit2Right
    child2 = [0] + fit2Left + fit1Right
    fitness(child1)
    fitness(child2)
    return [child1,child2]
    

def parentSelection(x,y):
    fit1 = mutate(x[slice(1,9)])
    fit2 = mutate(y[slice(1,9)])
    return crossover(fit1,fit2)

def removeLeastFit(x):
    x.pop()
    x.pop()
    #print(x)

# Sorts fitness based on number of conflicts
_queenFitness = sorted(_queenPlacement)

i = 2

fitness(_queenFitness[4])

# while i > 0:
#     print("Old:", _queenFitness)
#     removeLeastFit(_queenFitness)
#     _queenFitness += parentSelection(_queenFitness[0], _queenFitness[1])
#     _queenFitness = sorted(_queenFitness)
#     print("New:", _queenFitness)
#     i -= 1