## 지수 표현 방식

```python
# 1,000,000,000의 지수 표현 방식
a=1e9
print(a)

a=75.25e1
print(a)

a=3954e-3
print(a)
```

## 리스트

### 리스트 인덱싱과 슬라이싱

```python

a=[1,2,3,4,5,6,7]


# 뒤에서 첫 번쨰 원소
print(a[-1])
```

### 리스트 컴프리헨션

```python
array = [i for i in range(20) if i% 2 == 1]
print(array)

# [1,3,5,7,9,11,13,15,17,19]
```

### 백준 파이썬 입출력 정리

```python
a,b = input().split()
```
