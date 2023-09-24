"""
중복된 숫자가 input 으로 들어 오는 문제
하지만, 출력 하는 수열은 중복 되면 안됨
예를 들어, 9 7 9 1의 수열이 있다면, dfs 를 통해 완전 탐색 했을 때 [9, 7] 의 수열이 2번 나오게 된다.
"""


# dfs
def recur(cnt, arr):
    # 원하는 길이의 수열이 되었을 때
    if cnt == M:
        num_arr = [str(numbers[i]) for i in arr]
        num = " ".join(num_arr)
        # 그 수열이 존재 하지 않는다면 추가
        # 탐색 시간을 줄이기 위해 set 자료구조 사용
        # 리스트 형태로 set에 저장할 수 없으므로, 문자열로 변경
        if num not in result:
            result.add(num)
        return

    for idx in range(N):
        if idx in arr:
            continue
        recur(cnt+1, arr + [idx])


# 사전 순으로 출력 해야 하므로, 정렬 필요
N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

result = set()
recur(0, [])
# set 자료구조는 순서가 없으므로, 리스트로 변경 후 정렬하여 출력
result = list(result)

# 문자열 상태에서 정렬하면 안돼?
ans = []
for str_num in result:
    ans.append(list(map(int, str_num.split())))

ans.sort()
[print(*i) for i in ans]