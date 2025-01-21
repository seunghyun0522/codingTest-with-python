n = int(input())  # 풍선의 개수
a = list(map(int, input().split()))  # 풍선의 이동 값 리스트
indices = list(range(1, n + 1))  # 풍선의 원본 인덱스 (1-based)
result = []  # 결과를 저장할 리스트
idx = 0  # 현재 인덱스

while a:
    move = a[idx]  # 현재 풍선의 이동 값
    result.append(indices.pop(idx))  # 원본 인덱스를 결과에 추가
    a.pop(idx)  # 현재 풍선을 제거

    if not a:  # 리스트가 비었으면 종료
        break

    # 다음 인덱스 계산
    if move > 0:
        idx = (idx + move - 1) % len(a)  # 오른쪽으로 이동
    else:
        idx = (idx + move) % len(a)  # 왼쪽으로 이동

result = ' '.join(map(str, result))
print(result)
