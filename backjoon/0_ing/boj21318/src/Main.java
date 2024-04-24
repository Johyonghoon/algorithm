import java.util.*;
import java.io.*;

/*
누적합
 */

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());

        int[] difficulties = new int[N];
        int[] PREFIX = new int[N];
        st = new StringTokenizer(br.readLine());
        difficulties[0] = Integer.parseInt(st.nextToken());
        PREFIX[0] = 1;
        for (int i = 1; i < N; i++) {
            difficulties[i] = Integer.parseInt(st.nextToken());

            // 누적합
            if (difficulties[i-1] > difficulties[i]) PREFIX[i] = PREFIX[i-1];
            else PREFIX[i] = PREFIX[i-1] + 1;
        }

//        System.out.println("PREFIX = " + Arrays.toString(PREFIX));

        int Q = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < Q; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            sb.append((y - x) - (PREFIX[y-1] - PREFIX[x-1]));
            sb.append("\n");
        }

        System.out.println(sb);
    }
}