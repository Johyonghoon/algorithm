# 10610번 30
# https://www.acmicpc.net/problem/10610

N = int(input())
arr = list(map(int, list(str(N))))
arr.sort(reverse=True)
number = int("".join(str(i) for i in arr))
if sum(arr) % 3 == 0 and number % 10 == 0:
    print(number)
else:
    print(-1)

"""
N = int(input())
arr = list(map(int, list(str(N))))
arr.sort(reverse=True)
result = []
answer = -1
breaky = False

def recur():
    global answer, breaky
    if len(result) == len(arr):
        number = int("".join(str(arr[i]) for i in result))
        if number % 30 == 0:
            answer = max(number, answer)
            breaky = True
        return
    for idx in range(len(arr)):
        if idx in result:
            continue
        result.append(idx)
        recur()
        if breaky:
            break
        result.pop()

recur()

print(answer)
"""
