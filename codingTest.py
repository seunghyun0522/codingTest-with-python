n = int(input())

not_cute = 0
cute = 0

for i in range(n):
    vote = int(input())
    if(vote == 1):
        cute += 1
    else:
        not_cute += 1

print("Junhee is cute" if cute > not_cute else "Junhee is not cute!")