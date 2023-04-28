from itertools import permutations,combinations,product
import numpy as np

hor = [[1,2,3,4,5,6,7,8],
       [1,2,3,4,5,6,7,8],
       [1,2,3,4,5,6,7,8],
       [1,2,3,4,5,6,7,8],
       [1,2,3,4,5,6,7,8],
       [1,2,3,4,5,6,7,8],
       [1,2,3,4,5,6,7,8],
       [1,2,3,4,5,6,7,8]]

qArray = [1,2,3,4,5,6,7,8]

all = list(combinations(qArray,2))

diag = list(permutations([1,2,3,4,5,6,7,8]))
horSP = list(product(*hor))

print(len(diag)," -> search space for diagonal attacks only")
print(len(horSP)," -> search space for diagonal and horizontal attacks")
print(horSP[505141]) #horSP can contain diag permutation
print(diag[40319])
print(len(all)*2+8)


