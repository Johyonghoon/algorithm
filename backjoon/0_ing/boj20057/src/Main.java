import java.util.*;
import java.io.*;

/*
토네이도의 이동 (N/2, N/2) 위치에서 좌, 하, 우, 상 형태로 이동
1, 1, 2, 2, ... (N-1) (N-1) + (N-1) 만큼 이동
 */

public class Main {

    static int N;
    static int[][] graph;
    static int result;
    static int direction;
    static int[] dy = {0, 1, 0, -1};
    static int[] dx = {-1, 0, 1, 0};
    static int[] percent = {2, 10, 7, 1, 5, 10, 7, 1, 2};
    static int[] pdy = {-2, -1, -1, -1, 0, 1, 1, 1, 2, 0};
    static int[] pdx = {0, -1, 0, 1, -2, -1, 0, 1, 0, -1};

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        graph = new int[N][N];

        for (int y = 0; y < N; y++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int x = 0; x < N; x++) {
                graph[y][x] = Integer.parseInt(st.nextToken());
            }
        }

        // 토네이도 해당 방향 이동 횟수
        ArrayList<Integer> moveCnts = new ArrayList<>();
        for (int i = 1; i < N; i++) {
            moveCnts.add(i);
            moveCnts.add(i);
        }
        moveCnts.add(N - 1);

        int ny = N/2;
        int nx = N/2;
        direction = 0;
        for (int moveCnt : moveCnts) {
            for (int i = 0; i < moveCnt; i++) {
                ny += dy[direction];
                nx += dx[direction];
                tornado(ny, nx);
            }
            direction = (direction + 1) % 4;
        }
        result += graph[0][0];

        System.out.println(result);
    }

    static void tornado(int ny, int nx) {

        // 디버깅
//        System.out.println("ny: " + ny + " nx: " + nx + " direction: " + direction);
//        for (int y = 0; y < N; y++) {
//            for (int x = 0; x < N; x++) {
//                System.out.print(graph[y][x] + " ");
//            }
//            System.out.println();
//        }
//        System.out.println(result);

        int remainingSand = graph[ny][nx];
        for (int i = 0; i <= 9; i++) {
            int ey;
            int ex;
            if (direction == 0) {
                ey = ny + pdy[i];
                ex = nx + pdx[i];
            } else if (direction == 1) {
                ey = ny - pdx[i];
                ex = nx + pdy[i];
            } else if (direction == 2) {
                ey = ny - pdy[i];
                ex = nx - pdx[i];
            } else {
                ey = ny + pdx[i];
                ex = nx - pdy[i];
            }

            if (i == 9) {
                if (ey < 0 || ey >= N || ex < 0 || ex >= N) {
                    result += remainingSand;
                } else {
                    graph[ey][ex] += remainingSand;
                }
                continue;
            }

            int sand = graph[ny][nx] * percent[i] / 100;
            if (ey < 0 || ey >= N || ex < 0 || ex >= N) {
                result += sand;
                remainingSand -= sand;
                continue;
            }

            graph[ey][ex] += sand;
            remainingSand -= sand;
        }

        graph[ny][nx] = 0;

    }
}