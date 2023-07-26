# 1966번 프린터 큐
# https://www.acmicpc.net/problem/1966
import sys
from collections import deque
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    arr = []
    N, M = map(int, input().split())
    coordinate = deque()
    importance = list(map(int, input().split()))

    # idx번째 문서의 중요도를 중요도, idx 순서의 튜플로 저장
    for idx, impo in enumerate(importance):
        coordinate.append((impo, idx))

    cnt = 0
    while True:
        # coordinate 배열의 첫번째 값이 중요도가 가장 높다면 출력하기
        if coordinate[0][0] == max(coordinate)[0]:
            cnt += 1
            # 만약 M번째 문서가 출력되었다면 중단하고 cnt를 출력
            if coordinate.popleft()[1] == M:
                print(cnt)
                break
        else:
            # 중요도가 가장 높지 않다면 배열의 가장 뒤로 보내기
            temp = coordinate.popleft()
            coordinate.append(temp)
