# 16953번 A -> B
# https://www.acmicpc.net/problem/16953

A, B = map(int, input().split())


def recur(node, cnt):
    if node == B:
        result.append(cnt)
        return

    if node > B:
        return

    recur(node * 2, cnt+1)
    recur(int(str(node)+"1"), cnt+1)


result = []
recur(A, 1)
if result:
    result.sort()
    print(result[0])
else:
    print(-1)
