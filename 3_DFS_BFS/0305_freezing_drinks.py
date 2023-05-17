class FreezingDrinks:

    def solution(self, n, m):
        result = 0
        for i in range(n):
            for j in range(m):
                if self.dfs(i, j) == True:
                    result += 1
        print(result)

    def dfs(self, x, y):
        if x <= -1 or x >= n or y <= -1 or y >= m:
            return False
        if graph[x][y] == 0:
            graph[x][y] = 1
            self.dfs(x-1, y)
            self.dfs(x, y-1)
            self.dfs(x+1, y)
            self.dfs(x, y+1)
            return True
        return False


if __name__ == '__main__':
    n, m = map(int, input("얼음 틀의 세로 길이 N과 가로 길이 M을 입력하세요 : ").split())
    graph = []
    for i in range(n):
        graph.append(list(map(int, input(f"{i + 1}번째 얼음 틀의 형태를 입력하세요 : "))))
    FreezingDrinks().solution(n, m)
