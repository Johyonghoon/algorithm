import java.util.*;
import java.io.*;

public class Main {
    static int R;
    static int C;
    static int[][] graph;
    static boolean[][] visited;
    static int[] dy = new int[]{-1, 0, 1, 0};
    static int[] dx = new int[]{0, -1, 0, 1};

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        graph = new int[R][C];
        for (int y = 0; y < R; y++) {
            char[] arr = br.readLine().toCharArray();
            for (int x = 0; x < C; x++) {
                if (arr[x] == '.') graph[y][x] = 0;
                else if (arr[x] == '#') graph[y][x] = 9;
                else if (arr[x] == 'o') graph[y][x] = 1;
                else if (arr[x] == 'v') graph[y][x] = 2;
            }
        }

        visited = new boolean[R][C];
        int[] result = new int[]{0, 0};
        for (int y = 0; y < R; y++) {
            for (int x = 0; x < C; x++) {
                if (visited[y][x]) continue;

                int[] cnts = dfs(y, x, 0, 0);

                if (cnts[0] > cnts[1]) result[0] += cnts[0];
                else result[1] += cnts[1];
            }
        }

        System.out.println(result[0] + " "+ result[1]);
    }

    static int[] dfs(int ny, int nx, int o, int v) {
        visited[ny][nx] = true;
        int[] cnts = new int[]{o, v};
        if (graph[ny][nx] == 9) return cnts;
        else if (graph[ny][nx] == 1) cnts[0]++;
        else if (graph[ny][nx] == 2) cnts[1]++;

        for (int i = 0; i < 4; i++) {
            int ey = ny + dy[i];
            int ex = nx + dx[i];
            if (ey < 0 | ey >= R | ex < 0 | ex >= C) continue;
            if (visited[ey][ex]) continue;
            cnts = dfs(ey, ex, cnts[0], cnts[1]);
        }

        return cnts;
    }
}