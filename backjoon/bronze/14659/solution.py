# 14659번 한조서열정리하고옴ㅋㅋ
# https://www.acmicpc.net/problem/14659
import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

i = 0
# max 내장함수 사용 지양하는 중
maxi = 0
while True:
    cnt = 0
    # 모든 용은 오른쪽으로만 나아가기 때문에 자기 자신보다 큰 i+1번 인덱스부터 확인
    for j in range(i+1, N):
        if arr[i] > arr[j]:
            cnt += 1
        else:
            # 만약 arr[i] <= arr[j] 라면 그 지점부터 다시 시작
            # i 이후 j 이전의 값들은 모두 i의 cnt 개수보다 작기 때문
            i = j
            break
        # j가 끝날 때 모든 연산이 종료되어야 함
        if j == N-1:
            i = j
    if maxi < cnt:
        maxi = cnt
    if i == N-1:
        break

print(maxi)
