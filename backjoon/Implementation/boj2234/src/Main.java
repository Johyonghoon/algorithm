import java.util.*;
import java.io.*;

/**
 * 성곽, 굵은 선: 벽, 점선: 통로
 * 1. 이 성에 있는 방의 개수
 * 2. 가장 넓은 방의 넓이
 * 3. 하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방의 크기
 *   - 방의 벽을 제거하면 두 방의 크기의 합의 방이 생긴다.
 *   - 무작정 크다고 합칠 수 있는게 아니고, 인접한 방이어야 한다.
 *   - 성에는 최소 두 개의 방이 있어서, 항상 하나의 벽을 제거하여 두 방을 합치는 경우가 있다.
 * 그래프에 주어지는 정수 값은 서쪽: 1, 북쪽: 2, 동쪽: 4, 남쪽: 8
 */

public class Main {
    public static int N;
    public static int M;
    public static int[][][] graph;
    public static int[][] roomNum;
    public static int[] roomCnt = new int[2555];
    public static int[] dy = {0, -1, 0, 1};
    public static int[] dx = {-1, 0, 1, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        graph = new int[M][N][4];
        roomNum = new int[M][N];

        // M개의 줄, N개의 정수에 대한 벽의 정보
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                int num = Integer.parseInt(st.nextToken());
                for (int k = 0; k < 4; k++) {
                    graph[i][j][k] = num % 2;
                    num /= 2;
                }
            }
        }
//        System.out.println(Arrays.deepToString(graph));

        // 방 번호 등록
        int num = 0;
        for (int y = 0; y < M; y++) {
            for (int x = 0; x < N; x++) {
                if (roomNum[y][x] != 0) continue;
                num++;
                dfs(y, x, num);
            }
        }

        // 인접한 좌표 간 방 번호가 다를 때 방 크기 합쳐서 최대값 찾기
        int result2 = 0;
        int result3 = 0;
        for (int y = 0; y < M; y++) {
            for (int x = 0; x < N; x++) {
                int room1 = roomNum[y][x];
                result2 = Math.max(result2, roomCnt[room1]);
                for (int d = 0; d < 4; d++) {
                    int ey = y + dy[d];
                    int ex = x + dx[d];
                    if (0 <= ey && ey < M && 0 <= ex && ex < N) {
                        int room2 = roomNum[ey][ex];
                        if (room1 == room2) continue;
                        result3 = Math.max(result3, roomCnt[room1] + roomCnt[room2]);
                    }
                }
            }
        }

        // 결과 출력
        // 1. 이 성에 있는 방의 개수
        System.out.println(num);
        // 2. 가장 넓은 방의 크기
        System.out.println(result2);
        // 3. 하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방의 크기
        System.out.println(result3);
    }

    public static void dfs(int ny, int nx, int room) {
        roomNum[ny][nx] = room;
        roomCnt[room]++;
//        System.out.println("ny:" + ny + ", nx:" +nx + ", room:" + room);

        for (int d = 0; d < 4; d++) {
            if (graph[ny][nx][d] == 1) continue;  // 만약 벽이 있다면 패스
            int ey = ny + dy[d];
            int ex = nx + dx[d];
            if (0 <= ey && ey < M && 0 <= ex && ex < N) {
                if (roomNum[ey][ex] != 0) continue;  // 이미 방 번호가 결정되었다면 패스(부모 노드 포함)
                dfs(ey, ex, room);
            }
        }
    }
}