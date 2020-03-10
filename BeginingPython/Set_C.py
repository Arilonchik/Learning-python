import math
m,n = map(int,input().split())
print(math.factorial(m)/(math.factorial(n)*math.factorial(m-n)))
