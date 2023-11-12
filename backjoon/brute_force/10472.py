# 10472번 십자뒤집기
# https://www.acmicpc.net/problem/10472


"""
모든 칸이 흰색인 보드의 형태를 만들기
검은색 0 흰색 1
같은 칸을 두 번 뒤집으면 원래 상태로 돌아오게 된다.
따라서, 각 칸을 뒤집거나 뒤집지 않는 경우를 3*3에 적용하면 2**(3*3) = 512개의 경우의 수가 발생

"""
from collections import deque
from copy import deepcopy
from collections import defaultdict


class Problem:

    def __init__(self):
        global cases
        self.around_from = self.around()
        self.coordinate = self.make_coordinate()
        self.cases = cases

    def make_coordinate(self):
        c = []
        for y in range(3):
            for x in range(3):
                c.append((y, x))
        return c

    def to_matrix(self, string):
        matrix = []
        for i in range(3):
            matrix.append(list(string[i*3:i*3+3]))
        return matrix

    def to_string(self, matrix):
        string = ''
        for y in range(3):
            for x in range(3):
                string += matrix[y][x]
        return string

    def around(self):
        dp = [[[] for _ in range(3)] for _ in range(3)]
        delta = [[0, 0], [1, 0], [0, 1], [-1, 0], [0, -1]]
        for y in range(3):
            for x in range(3):
                for dy, dx in delta:
                    ey = y + dy
                    ex = x + dx
                    if 0 <= ey < 3 and 0 <= ex < 3:
                        dp[y][x].append((ey, ex))
        return dp

    def recur(self, idx, string, cnt):
        if idx == 9:
            self.cases[string] = cnt
            # print(string, self.cases[string])
            return

        # 뒤집거나
        self.recur(idx+1, string, cnt)

        # 뒤집지 않거나
        matrix = self.to_matrix(string)
        y, x = self.coordinate[idx]
        for ny, nx in self.around_from[y][x]:
            if matrix[ny][nx] == '1':
                matrix[ny][nx] = '0'
            elif matrix[ny][nx] == '0':
                matrix[ny][nx] = '1'
        new_string = self.to_string(matrix)
        self.recur(idx+1, new_string, cnt+1)


cases = defaultdict(int)
Problem().recur(0, '111111111', 0)
T = int(input())
for _ in range(T):
    S = ''
    for _ in range(3):
        S += input().replace('*', '0').replace('.', '1')
    print(cases[S])
