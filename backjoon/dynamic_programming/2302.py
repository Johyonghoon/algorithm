# 2302번 극장 좌석
# https://www.acmicpc.net/problem/2302

N = int(input())
M = int(input())

seats = [0 for _ in range(N)]
VIP = set()
for _ in range(M):
    seats[int(input())-1] = 1

i = 0
isVIP = False
result = []
cnt = 0
while i < N:
    if not isVIP:
        if seats[i]:
            isVIP = True
            result.append(cnt)
            cnt = 0
            i += 1
        else:
            cnt += 1
            i += 1
    else:
        if not seats[i]:
            isVIP = False
            result.append(1)
            cnt += 1
            i += 1
        else:
            i += 1

if isVIP:
    result.append(1)
else:
    result.append(cnt)


# print(result)
fibo = [1, 1]
for idx in range(2, 41):
    fibo.append(fibo[idx-1] + fibo[idx-2])

answer = 1
for idx in result:
    answer *= fibo[idx]

print(answer)



"""
# 1개 : 1
1

# 2개 : 2
1 2
2 1

# 3개 : 3
1 2 3
1 3 2
2 1 3

# 4개 : 5
1 2 3 4
1 2 4 3
1 3 2 4
2 1 3 4
2 1 4 3

# 5개 : 8
1 2 3 4 5
1 2 3 5 4
1 2 4 3 5
1 3 2 4 5
1 3 2 5 4
2 1 3 4 5
2 1 3 5 4
2 1 4 3 5
"""



"""
# 시간 초과, 재귀는 능사가 아니다,,,
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def recur(seat):
    global cnt
    # VIP 좌석은 이미 채워져 있으므로 패스
    if seat in VIP:
        recur(seat+1)
        return

    # 마지막 좌석까지 확인했을 때 모두 앉았다면 카운트
    if seat == N+1:
        if 0 not in peoples:
            cnt += 1
        return

    # 사람은 좌석 기준 1 작은수부터 1 큰수까지 앉을 수 있다
    for person in range(seat-1, seat+2):
        # VIP는 미리 자리에 앉혔다.
        if 0 < person <= N and person not in VIP:
            # 앉지 않은 사람이라면
            if not peoples[person]:
                # print(peoples, person)
                # 앉히고 dfs 탐색
                peoples[person] = 1
                recur(seat+1)
                peoples[person] = 0


N = int(input())
M = int(input())
VIP = set()
for _ in range(M):
    VIP.add(int(input()))

# VIP를 미리 자리에 앉히자
peoples = [0 for _ in range(N+1)]
peoples[0] = 1
for vip in VIP:
    peoples[vip] = 1

cnt = 0
recur(1)
print(cnt)
"""