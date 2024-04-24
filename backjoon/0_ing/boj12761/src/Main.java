import java.util.*;
import java.io.*;

public class Main {
    static int A;
    static int B;
    static int N;
    static int M;
    static int[] dist;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        A = Integer.parseInt(st.nextToken());
        B = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        // 이동가능방법 : +1, -1, +A, +B, -A, -B, idx * A, idx * B
        dist = new int[100_001];
        for (int i = 0; i <= 100_000; i++) {
            dist[i] = Integer.MAX_VALUE;
        }
        dist[N] = 0;

        bfs();
        System.out.println(dist[M]);
    }

    static void bfs() {
        Deque<Integer> q = new ArrayDeque();
        q.add(N);

        while (!q.isEmpty()) {
            int node = q.poll();
            if (node == M) break;

            if (node + 1 <= 100_000 && dist[node+1] > dist[node]+1) {
                dist[node + 1] = dist[node] + 1;
                q.add(node+1);
            }
            if (node - 1 >= 0 && dist[node-1] > dist[node]+1) {
                dist[node - 1] = dist[node] + 1;
                q.add(node-1);
            }
            if (node + A <= 100_000 && dist[node+A] > dist[node]+1) {
                dist[node + A] = dist[node] + 1;
                q.add(node+A);
            }
            if (node - A >= 0 && dist[node-A] > dist[node]+1) {
                dist[node - A] = dist[node] + 1;
                q.add(node-A);
            }
            if (node + B <= 100_000 && dist[node+B] > dist[node]+1) {
                dist[node + B] = dist[node] + 1;
                q.add(node+B);
            }
            if (node - B >= 0 && dist[node-B] > dist[node]+1) {
                dist[node - B] = dist[node] + 1;
                q.add(node-B);
            }
            if (node * A <= 100_000 && dist[node*A] > dist[node]+1) {
                dist[node * A] = dist[node] + 1;
                q.add(node * A);
            }
            if (node * B <= 100_000 && dist[node*B] > dist[node]+1) {
                dist[node * B] = dist[node] + 1;
                q.add(node * B);
            }
        }
    }
}