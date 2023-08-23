# 1182번 부분수열의 합
# https://www.acmicpc.net/problem/1182

N, S = map(int, input().split())
arr = list(map(int, input().split()))
sequence = []
cnt = 0

def recur(idx, total):
    global cnt
    if idx == N:
        if len(sequence) != 0 and sum(sequence) == S:
            cnt += 1
        return
    sequence.append(arr[idx])
    recur(idx+1, total+arr[idx])
    sequence.pop()
    recur(idx+1, total)

recur(0, 0)

print(cnt)
