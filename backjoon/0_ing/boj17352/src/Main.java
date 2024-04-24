import java.util.*;
import java.io.*;

public class Main {

    static int N;
    static ArrayList<ArrayList<Integer>> edges = new ArrayList<>();
    static boolean[] visited;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        visited = new boolean[N+1];

        // 간선 정보 등록
        for (int i=0; i <= N; i++) {
            edges.add(new ArrayList<>());
        }
        for (int i = 0; i < N - 2; i++) {
            st = new StringTokenizer(br.readLine());
            int v1 = Integer.parseInt(st.nextToken());
            int v2 = Integer.parseInt(st.nextToken());
            edges.get(v1).add(v2);
            edges.get(v2).add(v1);
        }

        // 하나의 다리만 제외하고는 다 연결되어 있는 듯 하니
        // 연결되어 있는 하나의 노드를 탐색
        // 혼자라 하더라도, 다른 애들이 지들끼리 붙어 있겠지 ㅋ
        dfs(1);

        int node = 0;
        for (int i = 2; i <= N; i++) {
            if (visited[i]) continue;
            node = i;
            break;
        }

        System.out.println(1 + " " + node);
    }

    static void dfs(int idx) {
        visited[idx] = true;

        for (int edge : edges.get(idx)) {
            if (visited[edge]) continue;
            dfs(edge);
        }
    }
}