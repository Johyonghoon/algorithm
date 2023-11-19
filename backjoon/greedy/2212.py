# 2212번 센서
# https://www.acmicpc.net/problem/2212

"""
고속도로 위 N개의 좌표에 센서가 있을 때 집중국을 적절히 설치하여 수신 가능영역 거리의 합의 최솟값을 구하는 문제
1개 이상의 센서를 가진 K개의 그룹을 만들어, 그 그룹의 최소값과 최대값의 차이의 합을 구한다.
각 구간의 차이를 구해, 차이가 큰 경우를 K-1개만큼 필터링하면, 그룹핑이 자연스레 이루어진다.
"""

from itertools import combinations


_N = int(input())
K = int(input())
sensors = list(set(map(int, input().split())))
sensors.sort()
N = len(sensors)

diff = []
for idx in range(1, N):
    diff.append(sensors[idx] - sensors[idx-1])
diff.sort()

print(sum(diff[:N-K]))
