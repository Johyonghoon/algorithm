import java.util.*;
import java.io.*;

public class Main {
    static int[] dy = {1, -1, 0, 0};
    static int[] dx = {0, 0, 1, -1};
    static int N;
    static int M;
    static int HX;
    static int HY;
    static int EX;
    static int EY;
    static int[][] graph;
    static int[][] dist;
    static int[][] distMagic;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        HY = Integer.parseInt(st.nextToken()) - 1;
        HX = Integer.parseInt(st.nextToken()) - 1;

        st = new StringTokenizer(br.readLine());
        EY = Integer.parseInt(st.nextToken()) - 1;
        EX = Integer.parseInt(st.nextToken()) - 1;

        graph = new int[N][M];
        for (int y = 0; y < N; y++) {
            st = new StringTokenizer(br.readLine());
            for (int x = 0; x < M; x++) {
                graph[y][x] = Integer.parseInt(st.nextToken());
            }
        }

        dist = new int[N][M];
        for (int y = 0; y < N; y++) {
            for (int x = 0; x < M; x++) {
                dist[y][x] = Integer.MAX_VALUE;
            }
        }
        dist[HY][HX] = 0;

        distMagic = new int[N][M];
        for (int y = 0; y < N; y++) {
            for (int x = 0; x < M; x++) {
                distMagic[y][x] = Integer.MAX_VALUE;
            }
        }

        bfs();

//        System.out.println(Arrays.deepToString(dist));

        if (dist[EY][EX] == Integer.MAX_VALUE && distMagic[EY][EX] == Integer.MAX_VALUE) {
            System.out.println(-1);
        } else {
            System.out.println(Math.min(dist[EY][EX], distMagic[EY][EX]));
        }

    }

    static void bfs() {
        Deque<Node> q = new ArrayDeque();
        Node node = new Node(HY, HX, false);
        q.add(node);

        while (!q.isEmpty()) {
            node = q.poll();
            int ny = node.ny;
            int nx = node.nx;
            boolean magic = node.magic;

            for (int d = 0; d < 4; d++) {
                int ey = ny + dy[d];
                int ex = nx + dx[d];
                if (ey < 0 || ey >= N || ex < 0 || ex >= M) continue;
                // 이미 벽을 부쉈을 때
                if (magic) {
                    // 벽이 없는 경우만 가능하므로
                    if (graph[ey][ex] == 0) {
                        // 이동거리가 최소인 경우
                        if (distMagic[ey][ex] > distMagic[ny][nx] + 1) {
                            distMagic[ey][ex] = distMagic[ny][nx] + 1;
                            q.add(new Node(ey, ex, magic));
                        }
                    }
                // 벽을 부수지 않았을 때
                } else {
                    // 1. 벽이 없는 경우
                    if (graph[ey][ex] == 0) {
                        // 이동거리가 최소인 경우
                        if (dist[ey][ex] > dist[ny][nx] + 1) {
                            dist[ey][ex] = dist[ny][nx] + 1;
                            q.add(new Node(ey, ex, magic));
                        }
                    // 2. 벽이 있는 경우
                    } else {
                        // 이동거리가 최소인 경우
                        if (distMagic[ey][ex] > dist[ny][nx] + 1) {
                            distMagic[ey][ex] = dist[ny][nx] + 1;
                            q.add(new Node(ey, ex, true));
                        }
                    }
                }
            }
        }
    }

    static class Node {
        int ny;
        int nx;
        boolean magic;

        public Node(int ny, int nx, boolean magic) {
            this.ny = ny;
            this.nx = nx;
            this.magic = magic;
        }
    }
}