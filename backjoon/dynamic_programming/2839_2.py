# 2839번 설탕 배달
# https://www.acmicpc.net/problem/2839

"""
다이나믹 프로그래밍 관점에서의 풀이
1. 예를 들어, 18kg의 설탕을 배달해야 한다고 가정하자.
2. 18kg의 설탕을 가져갈 수 있는 경우의 수는
  - 13kg 의 설탕을 배달할 때의 봉지 최소 개수 + 5kg 1개
  - 15kg 의 설탕을 배달할 때의 봉지 최소 개수 + 3kg 1개
3. 두 가지 경우의 수중 최소에 해당하는 개수를 배달하면 된다.
4. 즉, 이미 N-3kg, N-5kg 의 최소 개수를 계산해두었다면,
   이를 기반으로 최소 개수를 다시 계산할 수 있다는 뜻이 된다.
"""

N = int(input())

# 불가능할 경우를 대비하여 -1 을 미리 삽입 // 3kg, 5kg 경우를 추가
dp = [-1 for _ in range(5001)]  # N <= 5000
dp[3] = 1
dp[5] = 1

# 처음부터 탐색하며 저장
for idx in range(6, N+1):
    cnt1 = 5000
    cnt2 = 5000
    if dp[idx-3] != -1:
        cnt1 = dp[idx-3] + 1
    if dp[idx-5] != -1:
        cnt2 = dp[idx-5] + 1
    # 만약 둘 다 불가능하다면 dp[idx] 또한 불가하다.
    if dp[idx-3] == -1 and dp[idx-5] == -1:
        continue

    dp[idx] = min(cnt1, cnt2)

print(dp[N])

