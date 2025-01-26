n = int(input())  
a = list(map(int, input().split())) 
idx_list=[]
idx = 0
result =[]
for i in range(n):
    idx_list.append(i+1)



while a:
    move = a[idx]
    result.append(idx_list.pop(idx))
    a.pop(idx)

    if not a:
        break
    if move > 0:
        idx = (idx + move -1)%len(a)
    else:
        idx = (idx + move)%len(a)
    
   


result = ' '.join(map(str, result))
print(result)