import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] numbers = new int[N];  // 각 수는 10억 이하 자연수

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            numbers[i] = Integer.parseInt(st.nextToken());
        }

        int result = 1;
        int[] DP = new int[N];
        Arrays.fill(DP, 1);
        for (int i = 1; i < N; i++) {
            int target = numbers[i];
            for (int j = 0; j < i; j++) {
                if (numbers[j] >= target) continue;
                if (DP[i] >= DP[j] + 1) continue;
                DP[i] = DP[j] + 1;
            }
            result = Math.max(result, DP[i]);
        }

//        System.out.println("DP = " + Arrays.toString(DP));
        System.out.println(result);
    }
}