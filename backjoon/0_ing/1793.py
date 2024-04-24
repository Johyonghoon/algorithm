# 1793 타일링

"""
n=0
0

n=1
1

n=2
DP[n] = DP[n-1] + DP[n-2] * 2
"""

DP = [0 for _ in range(251)]
DP[0] = 1
DP[1] = 1
for i in range(2, 251):
    DP[i] = DP[i-1] + DP[i-2] * 2

while True:
    try:
        n = int(input())
        print(DP[n])

    except:
        break
