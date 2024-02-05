import java.util.*;
import java.io.*;

public class Main {
    public static int[][] graph;
    public static long[][] DP;
    // 항상 최단거리만 이동하기 때문
    public static int[] dy = {-1, 0};
    public static int[] dx = {0, -1};

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        // 가로: N, 세로: M
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        graph = new int[M+1][N+1];
        DP = new long[M+1][N+1];


        // 공사 중인 도로의 개수 K
        int K = Integer.parseInt(br.readLine());
        for (int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine());
            int ax = Integer.parseInt(st.nextToken());
            int ay = Integer.parseInt(st.nextToken());
            int bx = Integer.parseInt(st.nextToken());
            int by = Integer.parseInt(st.nextToken());
            if (ax + ay > bx + by) {
                int tx = ax;
                int ty = ay;
                ax = bx;
                ay = by;
                bx = tx;
                by = ty;
            }
            // 비트 마스킹
            if (ax < bx) graph[by][bx] |= (1 << 1);
            else graph[by][bx] |= (1 << 0);
        }
//        System.out.println(Arrays.deepToString(graph));

        // 최단거리 경우의 수 DP 탐색
        DP[0][0] = 1;

        // x = 0일 때
        for (int y = 1; y <= M; y++) {
            if ((graph[y][0] & (1 << 0)) == 0) {
                DP[y][0] += DP[y + dy[0]][0 + dx[0]];
            } else {
                break;
            }
        }
        // y = 0일 때
        for (int x = 1; x <= N; x++) {
            if ((graph[0][x] & (1 << 1)) == 0) {
                DP[0][x] += DP[0 + dy[1]][x + dx[1]];
            } else {
                break;
            }
        }

        for (int y = 1; y <= M; y++) {
            for (int x = 1; x <= N; x++) {
                for (int i = 0; i < 2; i++) {
                    if ((graph[y][x] & (1 << i)) == 0) {
                        DP[y][x] += DP[y + dy[i]][x + dx[i]];
                    }
                }
            }
        }

//        System.out.println(Arrays.deepToString(DP));
        System.out.println(DP[M][N]);
    }
}