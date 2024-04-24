import java.util.*;
import java.io.*;

public class Main {

    static int a;
    static int b;
    static int N;
    static int M;
    static ArrayList<ArrayList<Integer>> edges = new ArrayList<>();;
    static ArrayList<Integer> dist = new ArrayList<>();;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        a = Integer.parseInt(st.nextToken());
        b = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        for (int i = 0; i <= N; i++) {
            edges.add(new ArrayList<>());
            dist.add(Integer.MAX_VALUE);
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int v1 = Integer.parseInt(st.nextToken());
            int v2 = Integer.parseInt(st.nextToken());
            edges.get(v1).add(v2);
            edges.get(v2).add(v1);
        }

        bfs();

        if (dist.get(b) == Integer.MAX_VALUE) System.out.println(-1);
        else System.out.println(dist.get(b));

    }

    static void bfs() {
        Deque<Integer> q = new ArrayDeque<>();
        q.add(a);
        dist.set(a, 0);

        while (!q.isEmpty()) {
            int node = q.poll();

            for (int edge : edges.get(node)) {
                if (dist.get(node) + 1 >= dist.get(edge)) continue;
                dist.set(edge, dist.get(node) + 1);
                q.add(edge);
            }

        }
    }
}

