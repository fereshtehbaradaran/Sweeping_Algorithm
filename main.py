from countingSort import sort
import matplotlib.pyplot as plt
import numpy as np

# Inputs
n = int(input("Enter number of Affine Functions: "))
print("Enter ax + b as a,b in seperate lines:")
functions = [list(map(int, input().split(','))) for i in range(n)]


# Visualization
for i in range(n):
    plt.plot(np.array([-3, 3]), np.array([functions[i][0] * -3 + functions[i][1], functions[i][0] * 3 + functions[i][1]]))


# Sorting by the line slopes
sortedFunctions = sort(functions)


# Find min of max
currentFuncIndex = 0
visitedLines = []
minPoint = ""
minValue = -1
isFound = False

while not isFound:
    visitedLines.append(currentFuncIndex)
    a1, b1 = sortedFunctions[currentFuncIndex]
    f = lambda x: a1 * x + b1
    
    maxX = minPoint
    nextFuncIndex = currentFuncIndex
    
    for i in range(n):
        
        if i not in visitedLines:
            
            a2, b2 = sortedFunctions[i]
            temp = (b2 - b1) / (a1 - a2)
            
            if maxX == "" or f(temp) >= f(maxX):
                maxX = temp
                nextFuncIndex = i
            
                                    
    if minPoint == "" or (maxX > minPoint and f(maxX) < minValue):
        minPoint = maxX
        minValue = f(maxX)
    else:
        isFound = True
    
    currentFuncIndex = nextFuncIndex
    
print(minPoint, minValue)

plt.plot([minPoint], [minValue], 'o', color="red")
plt.show()        