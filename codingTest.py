# 2
# 3
# Yonsei 10
# Korea 10000000
# Ewha 20
# 2
# Yonsei 1
# Korea 10000000 


T = int(input())
result = []
for _ in range(T):
    max = 0
    max_univ = ""
    N = int(input())
    for _ in range(N):
        univ , beer = input().split()
        beer = int(beer)
        if beer > max :
            max = beer
            max_univ = univ
            
    result.append(max_univ)
            

print("\n".join(result))