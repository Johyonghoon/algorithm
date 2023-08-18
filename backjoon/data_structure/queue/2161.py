# 2161번 카드 1
# https://www.acmicpc.net/problem/2161

"""
1. 1~N까지의 카드 정보를 담은 circular queue 를 생성
2. 카드가 한 장 남을 때까지 enq, deq 반복하기
"""


# push
def enq(num):
    global rear
    rear = (rear+1) % cQsize
    cQ[rear] = num


# pop (?)
def deq():
    global front
    front = (front+1) % cQsize
    return cQ[front]


N = int(input())
cQsize = N
cQ = [i for i in range(1, N+1)]
front = -1
rear = N-1

result = []
while len(result) != N:
    # print(cQ)
    # print(result)
    result.append(deq())
    enq(deq())

print(*result)
