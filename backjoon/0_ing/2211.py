# 2211 네트워크 복구

"""
N개의 컴퓨터로 구성된 네트워크 (1 <= N <= 1000)
보안 시스템을 한 대의 슈퍼컴퓨터에만 설치 가능
1. 서로 다른 두 컴퓨터 간 통신이 가능하도록 회선을 복구하되 최소 개수의 회선만을 복구
2. 슈퍼컴퓨터가 다른 컴퓨터들과 통신하는데 걸리는 최소 시간이, 원래의 네트워크에서 통신하는데 걸리는 최소 시간보다 커져서는 안된다.
슈퍼컴퓨터는 1번 컴퓨터, 모든 통신은 양방향 통신
"""

import heapq


class Main:

    def __init__(self):

        self.N, self.M = map(int, input().split())

        # 간선 정보 기록
        self.edges = [[] for _ in range(self.N+1)]
        for i in range(self.M):
            # A번 컴퓨터와 B번 컴퓨터가 통신 시간이 C인 회선으로 연결되어 있다.
            A, B, C = map(int, input().split())
            self.edges[A].append([C, B])
            self.edges[B].append([C, A])

        # 최소시간 정보
        self.min_time = [int(1e9) for _ in range(self.N+1)]
        self.min_time[1] = 0

    def solution(self):
        # 최소 거리 구하기
        self.find_min_time_from_super_computer()

        # 최소 거리보다 짧은 거리의 최소 개수와 간선 찾기
        result = self.find_edges()

        print(len(result))
        for v1, v2 in result:
            print(v1, v2)

    def find_min_time_from_super_computer(self):
        pq = []
        heapq.heappush(pq, [0, 1])
        visited = [False for _ in range(self.N+1)]

        while pq:
            weight, node = heapq.heappop(pq)

            for w, nxt in self.edges[node]:

                if self.min_time[nxt] > weight + w:
                    self.min_time[nxt] = weight + w
                    heapq.heappush(pq, [self.min_time[nxt], nxt])

    def find_edges(self):
        pq = []
        heapq.heappush(pq, [0, 1])
        visited = [False for _ in range(self.N+1)]
        visited[1] = True
        result = []

        while pq:
            weight, node = heapq.heappop(pq)

            for w, nxt in self.edges[node]:
                # 이미 방문했다면 패스
                if visited[nxt]:
                    continue

                if self.min_time[nxt] < weight + w:
                    continue

                heapq.heappush(pq, [self.min_time[nxt], nxt])
                visited[nxt] = True
                result.append((node, nxt))

        return result


if __name__ == '__main__':
    main = Main()
    main.solution()

"""
3 3
1 2 2
1 3 1
2 3 1
"""