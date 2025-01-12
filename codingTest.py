S = input()
S = int(S)


cnt = 0
sum = 0
while True:
    cnt += 1
    sum += cnt
    
    if S < sum:
        break

        

print(cnt-1)