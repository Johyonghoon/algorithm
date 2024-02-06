import java.util.*;
import java.io.*;

public class Main {

    public static ArrayList<Integer>[] edges;
    public static int[] dist;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        edges = new ArrayList[N+1];
        for (int i = 1; i <= N; i++) {
            edges[i] = new ArrayList<>();
        }

        dist = new int[N+1];
        for (int i = 0; i <= N; i++) {
            dist[i] = Integer.MAX_VALUE;
        }
        dist[1] = 0;

        // 양방향 노드
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int n1 = Integer.parseInt(st.nextToken());
            int n2 = Integer.parseInt(st.nextToken());

            edges[n1].add(n2);
            edges[n2].add(n1);
        }

        bfs();

        // 1. 숨어야 하는 헛간 번호(거리가 같은 헛간이 여러 개면 가장 작은 헛간)
        // 2. 그 헛간까지의 거리
        // 3. 그 헛간과 같은 거리를 갖는 헛간의 개수
        int result1 = 0;
        int result2 = -1;
        int result3 = 0;

        for (int i = 1; i <= N; i++) {
            if (dist[i] > result2) {
                result1 = i;
                result2 = dist[i];
                result3 = 1;
            } else if (dist[i] == result2) {
                result3++;
            }
        }

//        System.out.println(Arrays.toString(dist));
        System.out.printf("%d %d %d", result1, result2, result3);
    }

    public static void bfs() {
        Deque<Integer> q = new ArrayDeque<>();
        q.add(1);

        while (!q.isEmpty()) {
            int node = q.remove();
            for (int nxt: edges[node]) {
                if (dist[nxt] > dist[node] + 1) {
                    dist[nxt] = dist[node] + 1;
                    q.add(nxt);
                }
            }
        }
    }
}