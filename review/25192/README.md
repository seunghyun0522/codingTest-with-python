## 25192 인사성 밝은 곰곰이

[link](https://www.acmicpc.net/problem/25192)

### 핵심 자료구조 set

- 사용한 이유 : 중복을 자동으로 제거하는 특성을 이용

```python

n = int(input())
chatList = set()  # 중복 제거를 위한 set
count = 0         # 총 카운트를 저장할 변수

for _ in range(n):
    chat = input()
    if chat == "ENTER":          # 새로운 입장
        count += len(chatList)   # 현재까지의 중복되지 않은 채팅 수 추가
        chatList.clear()         # set 초기화
    else:
        chatList.add(chat)       # 채팅 추가

count += len(chatList)  # 마지막 ENTER 이후의 채팅도 카운트

print(count)

```