import java.util.*;
import java.io.*;

/*
트리의 루트는 항상 1번 정점
맨 처음에는 모든 정점이 하얀색(0)으로 칠해져 있는 상태
 */

public class Main {

    static int N;
    static int[] nowColors;
    static int[] expectedColors;
    static boolean[] visited;
    static ArrayList<ArrayList<Integer>> edges = new ArrayList<>();

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        // 기본 정보
        N = Integer.parseInt(br.readLine());
        nowColors = new int[N+1];
        expectedColors = new int[N+1];
        visited = new boolean[N+1];

        // 정점의 색깔 정보
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            expectedColors[i] = Integer.parseInt(st.nextToken());
        }

        // 간선 정보
        for (int i = 0; i <= N; i++) {
            edges.add(new ArrayList<>());
        }

        for (int i = 0; i < N - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            // 양방향으로 만들기는 해야하나봄
            edges.get(a).add(b);
            edges.get(b).add(a);
        }

        int result = 0;
        for (int i = 1; i <= N; i++) {
            if (visited[i]) continue;
            result += bfs(i);
        }

        System.out.println(result);
    }

    private static int bfs(int idx) {
        Deque<Node> q = new ArrayDeque<>();
        q.add(new Node(idx, 0, nowColors[idx]));
        int result = 0;

        while (!q.isEmpty()) {
            Node node = q.poll();
            int now = node.now;
            int color = node.color;
            nowColors[now] = color;
//            System.out.println("now = " + now);
//            System.out.println("color = " + color);
//            System.out.println("nowColors = " + nowColors[now]);
//            System.out.println("expectedColor = " + expectedColors[now]);

            // 이미 방문했다면 패스
            if (visited[now]) continue;

            // 방문 처리
            visited[now] = true;

            // 현재 색깔이 다르다면 색칠하기
            if (nowColors[now] != expectedColors[now]) {
                result++;
            }

            for (int edge : edges.get(now)) {
                if (edge == now) continue;

                q.add(new Node(edge, now, expectedColors[now]));
            }
        }

        return result;
    }

    static class Node {
        private int now;
        private int prnt;
        private int color;

        public Node(int now, int prnt, int color) {
            this.now = now;
            this.prnt = prnt;
            this.color = color;
        }
    }
}