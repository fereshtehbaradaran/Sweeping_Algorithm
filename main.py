from countingSort import sort
import matplotlib.pyplot as plt
import numpy as np

# Inputs
n = int(input("Enter number of Affine Functions: "))
print("Enter ax + b as a,b in seperate lines:")
functions = [list(map(int, input().split(','))) for i in range(n)]


# Visualization
fig = plt.figure()
ax = fig.add_subplot()
for a, b in functions:
    ax.plot(np.array([-3, 3]), np.array([a * -3 + b, a * 3 + b]))


# Sorting by the line slopes
sortedFunctions = sort(functions)
print(sortedFunctions)

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
        
        a2, b2 = sortedFunctions[i]
        
        if i not in visitedLines and a1 != a2:
            
            temp = (b2 - b1) / (a1 - a2)
            
            if maxX == "" or temp <= maxX:
                maxX = temp
                nextFuncIndex = i
            
                                    
    if minPoint == "" or (maxX > minPoint and f(maxX) < minValue):
        minPoint = maxX
        minValue = f(maxX)
    else:
        isFound = True
    
    currentFuncIndex = nextFuncIndex
    
print(minPoint, minValue)

ax.plot([minPoint], [minValue], 'o', color="red")
ax.text(minPoint - 1, minValue + 3, "%.2f, %.2f" %(minPoint, minValue), style='italic',bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 5})
plt.show()     