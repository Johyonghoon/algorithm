# 13397번 구간 나누기 2
# https://www.acmicpc.net/problem/13397

"""
# 이분탐색 - 파라메트릭 서치
"""

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

start = 0
end = max(numbers)-1
result = end

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    left = 0
    right = left+1
    while right <= N:
        arr = numbers[left:right]
        if max(arr) - min(arr) > mid:
            left = right - 1
            right = left + 1
            cnt += 1
        else:
            right += 1
        # 끝까지 탐색했을 때 배열이 존재한다면 카운트
        if right == N+1:
            if arr:
                cnt += 1
        # print(arr, mid, cnt, right)
    if cnt <= M:
        result = min(result, mid)
        end = mid - 1
    else:
        start = mid + 1

print(result)


