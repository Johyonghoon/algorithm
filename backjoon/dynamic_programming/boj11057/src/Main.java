import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 마지막 숫자의 개수를 저장해서, 그 수의 개수 * 다음으로 올 수 있는 수의 개수의 합
 */

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int[][] DP = new int[N+1][10];

        // 1번째 DP 저장
        for (int i = 0; i < 10; i++) {
            DP[1][i] = 1;
        }

        for (int i = 2; i <= N; i++) {
            for (int j = 0; j < 10; j++) {
                for (int k = j; k < 10; k++) {
                    DP[i][k] = (DP[i][k] + DP[i - 1][j]) % 10_007;
                }
            }
        }

        int result = 0;
        for (int i = 0; i < 10; i++) {
            result += DP[N][i];
        }
        System.out.println(result % 10_007);
    }
}