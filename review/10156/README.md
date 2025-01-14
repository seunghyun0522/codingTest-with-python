### 돈 필요할때(만) 부모님 찾는 효자;;

k = 과자 한 개의 가격
n = 사려고 하는 과자의 개수
m = 현재 가진 돈의 액수

```python
k,n,m = input().split()
k = int(k)
n = int(n)
m = int(m)
print(k*n-m if k*n-m>0 else 0)
```
