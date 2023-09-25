# 2785번 체인
# https://www.acmicpc.net/problem/2785

"""
가장 짧은 길이의 체인을 하나씩 분해하여 연결에 사용한다.
이때, 연결해주는 체인은 가장 긴 체인을 두개 먼저 연결하고,
다음 체인부터 하나씩 연결하게 된다.
"""

from collections import deque


N = int(input())
q = deque(sorted(list(map(int, input().split()))))

cnt = 0
link = 0
while len(q) > 1:
    link = q.popleft()
    while link and len(q) > 1:
        chain = q.pop()
        chain += q.pop()
        q.append(chain)
        link -= 1
        cnt += 1
        # print(q, cnt, link)

# 연결에 사용하는 체인이 1개라도 남아 있다면 긴 체인에 연결하기 위해 한 개를 열어준다.
if link:
    cnt += 1

print(cnt)
