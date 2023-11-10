from countingSort import sort
import matplotlib.pyplot as plt
import numpy as np


n = int(input("Enter number of Affine Functions: "))
print("Enter ax + b as a,b in seperate lines:")
functions = [list(map(int, input().split(','))) for i in range(n)]

for i in range(n):
    plt.plot(np.array([-3, 3]), np.array([functions[i][0] * -3 + functions[i][1], functions[i][0] * 3 + functions[i][1]]))
    
plt.show()