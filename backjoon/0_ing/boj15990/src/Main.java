import java.util.*;
import java.io.*;

/*
N=1
1
N=2
2
N=3
1+2
2+1
3
N=4
 */

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        long[][] DP = new long[100_001][4];
        DP[1][1] = 1;
        DP[2][2] = 1;
        DP[3][1] = 1;
        DP[3][2] = 1;
        DP[3][3] = 1;

        for (int i = 4; i <= 100_000; i++) {
            DP[i][1] = (DP[i-1][2] + DP[i-1][3]) % 1_000_000_009;
            DP[i][2] = (DP[i-2][1] + DP[i-2][3]) % 1_000_000_009;
            DP[i][3] = (DP[i-3][1] + DP[i-3][2]) % 1_000_000_009;
        }

        int T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++) {
            int N = Integer.parseInt(br.readLine());
            System.out.println((DP[N][1] + DP[N][2] + DP[N][3]) % 1_000_000_009);
//            System.out.println(Arrays.deepToString(DP));
//            System.out.println("DP[N][1] = " + DP[N][1]);
//            System.out.println("DP[N][2] = " + DP[N][2]);
//            System.out.println("DP[N][3] = " + DP[N][3]);
        }
    }
}