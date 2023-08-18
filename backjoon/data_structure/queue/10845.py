# 10845번 큐
# https://www.acmicpc.net/problem/10845

"""
python list를 활용하여 풀어보자.
"""
import sys
input = sys.stdin.readline


N = int(input())
queue = []
for idx in range(N):
    arr = list(input().split())
    command = arr[0]
    if command == "push":
        queue.append(int(arr[1]))
    elif command == "pop":
        if queue:
            print(queue.pop(0))
        else:
            print(-1)
    elif command == "size":
        print(len(queue))
    elif command == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif command == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)


"""
Linear Queue 구현
앞으로 다시는 이런 방법을 하지 말자.

import sys
input = sys.stdin.readline


# push
def enq(num):
    global rear, front
    if is_empty():
        front = rear = 0
    else:
        rear += 1
    Q[rear] = num


# pop
def deq():
    global rear, front
    if is_empty():
        return -1
    num = Q[front]
    if front == rear:
        front = rear = -1
    else:
        front += 1
    return num


# isEmpty
def is_empty():
    return front == -1


Qsize = 10_001  # 10,000개의 명령
Q = [0 for _ in range(Qsize)]
front = -1
rear = -1

N = int(input())
for idx in range(N):
    arr = list(input().split())
    command = arr[0]
    if command == "push":
        enq(int(arr[1]))
    elif command == "pop":
        print(deq())
    elif command == "size":
        if is_empty():
            print(0)
        else:
            print(rear - front + 1)
    elif command == "empty":
        print(int(is_empty()))
    elif command == "front":
        if Q[front]:
            print(Q[front])
        else:
            print(-1)
    elif command == "back":
        if Q[rear]:
            print(Q[rear])
        else:
            print(-1)
    # print(Q[:idx+1])
"""