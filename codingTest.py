import math
m = int(input())
n = int(input())
sum = 0 
min = n
for i in range(m, n+1):
    if math.sqrt(i) == int(math.sqrt(i)):
        sum += i
        if min > i:
            min = i

if sum > 0:
    print(sum)
    print(min)
else:
    print(-1)