def backtracking(node, arr, total):
    global isFilter
    if total == num:
        # print(num, total, arr)
        ls = list(arr) + [num_idx]
        ls.sort(reverse=True)
        for k in ls:
            ability.pop(k)
        isFilter = True
        return

    if node == len(ability):
        return

    for j in range(num_idx+1, L):
        if j in arr:
            continue
        if total+ability[j] > num:
            continue
        arr.add(j)
        # print(j, arr)
        backtracking(node+1, arr, total+ability[j])
        arr.remove(j)

        if isFilter:
            return


def recur(node, arr, total):
    global result

    if 0 < node <= L//2:
        another = sumi - total
        # print(another, total)
        result = min(result, abs(another - total))

    if node == L//2:
        return

    for j in range(L):
        if j in arr:
            continue
        arr.add(j)
        recur(node+1, arr, total+ability[j])
        arr.remove(j)


N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

ability = []
for y in range(N):
    for x in range(y+1, N):
        ability.append(graph[y][x] + graph[x][y])

# 최댓값을 먼저 탐색하며, 다른 값들의 합으로 만들 수 있는 수라면, 같이 제거
ability.sort(reverse=True)
print(ability)

idx = 0
while idx < len(ability):
    num = ability[idx]
    num_idx = idx
    L = len(ability)

    isFilter = False
    backtracking(0, set(), 0)
    if not isFilter:
        idx += 1
    # print(idx, ability)

print(ability)
sumi = sum(ability)
L = len(ability)
result = 10**9
recur(0, set(), 0)

# print(ability)
if result == 10**9:
    print(0)
else:
    print(result)
