# 6603번 로또
# https://www.acmicpc.net/problem/6603

def recur(node, prv, result):
    if node == 6:
        [print(S[i], end=' ') for i in result]
        print()
        return

    for nxt in range(prv + 1, k):
        if nxt < prv:
            continue
        result.append(nxt)
        recur(node + 1, nxt, result)
        result.pop()


while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    else:
        k = arr[0]
        S = arr[1:]
        recur(0, -1, [])
    print()
