import java.util.*;
import java.io.*;

/*
모든 칸에 k만큼의 수를 더하거나 빼면
최악의 경우 N개의 숫자에 M번만큼 연산을 수행하게 되므로 시간초과 발생
더하기 시작점에 + 끝난 후 -해서 누적해서 연산할 수 있도록!

1   2   3   4   5   -1  -2  -3  -4  -5
-3  -3  -3  -3  -3
                    5   5   5   5   5
    2   2   2   2   2   2
-3                  3
                    5
    2                       -2

 */

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] Heights = new int[N+1];
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            Heights[i] = Integer.parseInt(st.nextToken());
        }

        int[] PREFIX = new int[N+1];
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            // k<0일 경우 a~b칸까지 높이가 각각 |k|만큼 줄어들도록 흙을 파야하고,
            // k>=0일 경우 a~b칸까지 높이가 각각 |k|만큼 늘어나도록 흙을 파야함
            int k = Integer.parseInt(st.nextToken());
            PREFIX[a] += k;
            if (b < N) PREFIX[b+1] -= k;
        }

        // 결과 출력
        int total = 0;
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= N; i++) {
            total += PREFIX[i];
            sb.append((Heights[i] + total) + " ");
        }

        System.out.println(sb);
    }
}