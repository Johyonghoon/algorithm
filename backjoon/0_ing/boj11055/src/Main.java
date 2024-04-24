import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] numbers = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            numbers[i] = Integer.parseInt(st.nextToken());
        }

        int[] DP = new int[N];

        int result = numbers[0];
        for (int i = 0; i < N; i++) {
            DP[i] = numbers[i];
            for (int j = 0; j < i; j++) {
                if (numbers[i] > numbers[j] && DP[i] < DP[j] + numbers[i]) {
                    DP[i] = DP[j] + numbers[i];
                    result = Math.max(result, DP[i]);
                }
            }
        }

//        System.out.println("DP = " + Arrays.toString(DP));
        System.out.println(result);
    }
}