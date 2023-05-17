from collections import deque


class EscapeTheMaze:

    def solution(self, n, m):
        global dx, dy
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        print(self.bfs(0, 0))

    def bfs(self, x, y):
        queue = deque()
        queue.append((x, y))
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if graph[nx][ny] == 0:
                    continue
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))
        return graph[n-1][m-1]


if __name__ == '__main__':
    n, m = map(int, input("미로의 세로 길이 N과 가로 길이 M을 입력하세요 : ").split())
    graph = []
    for i in range(n):
        graph.append(list(map(int, input(f"{i + 1}번째 미로의 정보를 입력하세요 : "))))
    EscapeTheMaze().solution(n, m)
