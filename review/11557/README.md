### Yangjojang of The Year

- 술 어디가 잘 먹는지 시합 하는 문제

- join 사용하지 않으면 runtime error

```python

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
```
