import random
from matplotlib import pyplot
queen = [1,2,3,4,5,6,7,8]
numOfSol = 0
sol = []

def fitness(x):
    for i in range(len(x)-1):
        for j in range(i+1,len(x)):
            if abs(x[i]-x[j]) == abs(i-j):
                return
    return 0

def sim():
    global sol, numOfSol
    shuf = queen
    while numOfSol < 92:
        random.shuffle(shuf)
        f = fitness(shuf)
        if f == 0:
            shuf = []+shuf
            sol.append(shuf)
        if len(sol) > 100:
            sol = checkDupe(sol)
            numOfSol = len(sol)

def checkDupe(x):
    tmp = set()
    for i in x:
        tmp.add(tuple(i))
    s=list(tmp)
    return s

sim()
print(len(sol))
#-----------------------------------------------------------------------------


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
        data[x[i]-1][i] = 2
    return data

i=0
it = 0
while i<5:
    dataSol.append(convert(sol[i]))
    #print(dataSol[i])
    defaultData()
    i+=1
    

for i in range(len(dataSol)):
    pyplot.figure(figsize=(5,5),num=i)
    pyplot.imshow(dataSol[i])

pyplot.show()