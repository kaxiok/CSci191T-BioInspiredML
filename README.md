# CSci191T-BioInspiredML
CSUF-Spring-2023

How to install numpy for Windows
- python.exe -m pip install numpy or pip3 install numpy
- python.exe -m pip install --upgrade pip

How to install matplotlib
- pip3 install matplotlib

N Queens
- 8x8 size
- total combination of arrangement for size 8 is 64/((64-8)!/8!) = 4,426,165,368
- select array size for simulation.
- conflicts are a sum of the number of queens attacked

N Queens rules
- No horizontal conflict
- No vertical conflict
- No diagonal conflict

N Queens algorithm
- Fittest queen will have the least conflict
- Sort by most fit to least fit.
- Parent Selection. Pair fittest parents to create new child
- Survivor Selection. Remove least fittest queens to make space for new queen
- Mutation, Recombination, 
