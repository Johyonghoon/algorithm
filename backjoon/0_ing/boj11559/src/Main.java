import java.util.*;
import java.io.*;

public class Main {

    static char[][] graph = new char[12][6];
    static boolean[][] visited;
    static int[] dy = {1, -1, 0, 0};
    static int[] dx = {0, 0, 1, -1};
    static boolean isOverFour;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int i = 0; i < 12; i++) {
            String line = br.readLine();
            for (int j = 0; j < 6; j++) {
                graph[i][j] = line.toCharArray()[j];
            }
        }

        boolean isBomb = true;
        while (isBomb) {

            // 초기화
            isBomb = false;
            visited = new boolean[12][6];

            for (int y = 0; y < 12; y++) {
                for (int x = 0; x < 6; x++) {
                    if (visited[y][x]) continue;
                    isOverFour = false;
                    dfs(y, x, graph[y][x], 1);
                }
            }
        }
    }

    static void dfs(int ny, int nx, char target, int cnt) {
        visited[ny][nx] = true;

        for (int d = 0; d < 4; d++) {
            int ey = ny + dy[d];
            int ex = nx + dx[d];
            if (ey < 0 || ey >= 12 || ex < 0 || ex >= 6) continue;

        }
    }
}