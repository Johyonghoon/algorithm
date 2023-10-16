# 15685번 드래곤 커브
# https://www.acmicpc.net/problem/15685

"""
2차원 좌표 평면 위에서 세 가지 속성 (x축 방향 ->, y축 방향 아래 // 평상시 내가 하는 좌표 탐색)
1. 시작 점     (y, x)

            direction   0       1        2        3
2. 시작 방향    delta = [[0, 1], [-1, 0], [0, -1], [1, 0]]
3. 세대

K(K > 1)세대 드래곤 커브는 K-1 세대 드래곤 커브를 끝 점을 기준으로 90도 시계 방향 회전
그것을 끝 점에 붙인 것
=> 90도 회전의 의미? y = x 축을 기준으로 반대로 뒤집은 것
   but, 위 방향이 y축의 음의 방향이므로 주의

각 세대별 좌표를 구해봅시다.
x, y = 드래곤 커브의 시작 점
d = 시작 방향
g = 세대
0세대 : (y, x)                                    -> (y+direction[d][0], x+direction[d][1])
1세대 : (y+direction[d][0], x+direction[d][1])    ->
"""