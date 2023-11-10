


n = int(input("Enter number of Affine Functions: "))
print("Enter ax + b as a,b in seperate lines:")
functions = [list(map(int, input().split(','))) for i in range(n)]