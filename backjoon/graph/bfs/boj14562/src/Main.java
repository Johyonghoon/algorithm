import java.io.*;
import java.util.*;

public class Main {

    static void bfs(int score, int target) {
        Deque<int[]> q = new ArrayDeque<>();
        q.add(new int[]{score, target, 0});

        while (!q.isEmpty()) {
            int[] current = q.poll();
            int s = current[0];
            int t = current[1];
            int cnt = current[2];

            // 만약 s == t 라면 cnt 출력 후 종료
            if (s == t) {
                System.out.println(cnt);
                break;
            }

            // 1. A의 점수 s * 2 & B의 점수 t + 3
            if (s * 2 <= t + 3) {
                q.add(new int[]{s * 2, t + 3, cnt + 1});
            }

            // 2. A의 점수 s + 1
            q.add(new int[]{s + 1, t, cnt + 1});
        }
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int C = Integer.parseInt(st.nextToken());
        for (int i = 0; i < C; i++) {
            st = new StringTokenizer(br.readLine());
            int S = Integer.parseInt(st.nextToken());
            int T = Integer.parseInt(st.nextToken());

            bfs(S, T);
        }
    }
}