import java.util.*;
import java.io.*;

/*
바이러스를 막을 수 있는 벽을 3개 세워 안전 영역을 최대로 했을 때 안전 영역 크기의 최대값 구하기
3 <= N, M <= 8
그래프 크기가 작아서 벽을 놓을 수 있는 모든 경우를 탐색해봐도 괜찮으려나
0: 빈칸, 1: 벽, 2: 바이러스
 */

public class Main {
    static int[] dy = {-1, 1, 0, 0};
    static int[] dx = {0, 0, -1, 1};
    static int N;
    static int M;
    static int[][] graph;
    static ArrayList<int[]> virus;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        // 그래프 그리기 + 빈 칸 / 바이러스 찾기
        graph = new int[N][M];
        virus = new ArrayList<>();
        ArrayList<int[]> coor = new ArrayList<>();
        for (int y = 0; y < N; y++) {
            st = new StringTokenizer(br.readLine());
            for (int x = 0; x < M; x++) {
                graph[y][x] = Integer.parseInt(st.nextToken());
                int[] c = {y, x};
                if (graph[y][x] == 0) coor.add(c);
                else if (graph[y][x] == 1) virus.add(c);
            }
        }

        // 벽의 위치 3개 정하기 bfs 탐색
        int result = 0;
        for (int a = 0; a < coor.size(); a++) {
            graph[coor.get(a)[0]][coor.get(a)[1]] = 1;
            for (int b = a + 1; b < coor.size(); b++) {
                graph[coor.get(b)[0]][coor.get(b)[1]] = 1;
                for (int c = b + 1; c < coor.size(); c++) {
                    graph[coor.get(b)[0]][coor.get(b)[1]] = 1;
                    result = Math.max(result, bfs());
                    graph[coor.get(b)[0]][coor.get(b)[1]] = 0;
                }
                graph[coor.get(b)[0]][coor.get(b)[1]] = 0;
            }
            graph[coor.get(a)[0]][coor.get(a)[1]] = 0;
        }

    }

    static int bfs() {
        int cnt = 0;
        Deque<int[]> q = new ArrayDeque<>(virus);
        while (!q.isEmpty()) {
            int[] c = q.poll();
            int ny = c[0];
            int nx = c[1];

            for (int d = 0; d < 4; d++) {
                int ey = ny + dy[d];
                int ex = nx + dx[d];
                if (ey < 0 || ey >= N || ex )

            }

        }

        return cnt;
    }
}