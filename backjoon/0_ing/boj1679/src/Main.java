import java.util.*;
import java.io.*;

/*
1
1 1
3
3 1
3 1 1
3 3
3 3 1
3 3 1 1
3 3 3
3 3 3 1
3 3 3 1 1
3 3 3 3
3 3 3 3 1
3 3 3 3 1 1 => 총 사용 개수 6개로 실패
큰 수부터 백트래킹?
 */

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        // 크기 순으로 주어진다.
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] numbers = new int[N];
        for (int i = 0; i < N; i++) {
            numbers[i] = Integer.parseInt(st.nextToken());
        }

        int K = Integer.parseInt(br.readLine());

        int target = 1;
        boolean isTrue = true;
        while (isTrue) {
            target++;
            isTrue = false;
            int cnt = 0;
            int remain = target;
            for (int i = N - 1; i >= 0; i--) {
                cnt += remain / numbers[i];
                remain %= numbers[i];
                if (cnt > K) break;
                if (i == 0) isTrue = true;
            }
        }

        if (target % 2 == 1) System.out.println("jjaksoon win at " + target);
        else System.out.println("holsoon win at " + target);
    }
}