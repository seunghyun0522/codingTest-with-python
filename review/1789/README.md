~~input = sum(1~N)~~

~~output = N <- `N 구하기`~~

~~### 공식 사용하기~~

~~`1~N의 합 = n * (n+1) / 2`~~

### answer

```python

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
```
