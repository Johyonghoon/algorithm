import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        int[][] graph = new int[N+1][2];
        int[][] DP = new int[N+1][2];

        int result = 0;
        int grade = 0;
        for (int y = 1; y <= N; y++) {
            st = new StringTokenizer(br.readLine());

            for (int x = 0; x < 2; x++) {
                graph[y][x] = Integer.parseInt(st.nextToken());
                if (graph[y][x] == graph[y-1][x]) {
                    DP[y][x] = DP[y-1][x] + 1;
                } else if (graph[y][x] == graph[y-1][1-x]) {
                    DP[y][x] = DP[y-1][1-x] + 1;
                } else {
                    DP[y][x] = 1;
                }

                if (result < DP[y][x]) {
                    result = DP[y][x];
                    grade = graph[y][x];
                }
                else if (result == DP[y][x]) grade = Math.min(grade, graph[y][x]);
            }
        }
//        System.out.println(Arrays.deepToString(DP));
        System.out.println(result + " " + grade);

    }
}