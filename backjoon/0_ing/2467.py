# 2467번 용액
# https://www.acmicpc.net/problem/2467

N = int(input())
numbers = list(map(int, input().split()))

start = 0
end = start + 1

# 합의 최소를 찾고 그 두 값을 result 배열에 저장
mini = 2_000_000_001
result = []
# end의 최대 인덱스가 N-1이므로 N-1보다 작을 때 반복
while start < N-1:
    # 시작첨의 차이 초기화
    # pre = 2_000_000_001
    # end 포인터를 전체 탐색하되
    while end < N:
        diff = abs(numbers[start] + numbers[end])
        # print(diff, numbers[start], numbers[end])
        if mini > diff:
            mini = diff
            # if mini > pre:
            #     mini = pre
            result = [numbers[start], numbers[end]]
            end += 1
        # 차이가 더 커진다면 종료시키기
        else:
            # print(start, end)
            break

    # 탐색이 끝났다면 start를 한 칸 땡겨서 다시 탐색
    start += 1
    end = start + 1

print(*result)


"""
-99 -2 -1 4 98
-99 -2 101
-99 -1 100
-99 4 95
-99 98 1
-2 -1 3
-2 4 2
-2 98 96
-1 4 3
-1 98 97
4 98 102
-99 4 -95
-2 98 -
"""