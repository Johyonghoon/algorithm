# 20364번 부동산 다툼
# https://www.acmicpc.net/problem/20364

"""
이진 트리 모양의 땅에 번호를 입력
루트 노드로부터 출발하여, 원하는 땅의 노드까지 도달하는 중에 이미 오리가 존재하는 땅이 있다면 실패
"""

import sys
from collections import deque
input = sys.stdin.readline

N, Q = map(int, input().split())
nodes = [0 for _ in range(N+1)]
ducks = deque()
for _ in range(Q):
    ducks.append(int(input()))

while ducks:
    duck = ducks.popleft()
    isPossible = True
    result = 0
    idx = duck
    # 부모 노드를 거슬러 올라가며 이미 오리가 점유하고 있다면 result 업데이트
    # 중복된 땅도 원할 수 있는건가..? 해당 땅부터 확인
    while idx:
        # 경로 상에 오리가 점유하고 있으므로 result를 업데이트
        if nodes[idx]:
            result = idx
            isPossible = False

        idx //= 2

    # 오리를 만나지 않았다면, 해당 노드에 배치하고 0을 출력
    if isPossible:
        nodes[duck] = 1
        print(0)
    # 만났다면, 가장 가까이서 만난 노드를 출력
    else:
        print(result)
