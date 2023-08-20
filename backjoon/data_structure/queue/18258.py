# 18258번 큐 2
# https://www.acmicpc.net/problem/18258

import sys
input = sys.stdin.readline


def is_empty():
    return front == rear


def enq(num):
    global rear, front
    if is_empty():
        rear = front = 0
    rear = (rear+1) % N
    Q[rear] = num


def deq():
    global front
    front = (front+1) % N
    return Q[front]


N = int(input())    # 2_000_000
# queue
Q = [0 for _ in range(N)]
front = -1
rear = -1

for idx in range(N):
    arr = list(input().split())
    command = arr[0]

    if command == "push":
        enq(int(arr[1]))
    elif command == "pop":
        if is_empty():
            print(-1)
        else:
            print(deq())
    elif command == "size":
            print(rear - front)
    elif command == "empty":
        print(int(is_empty()))
    elif command == "front":
        print(Q[front+1])
    elif command == "back":
        print(Q[rear])

    # print(Q[:idx+1])

