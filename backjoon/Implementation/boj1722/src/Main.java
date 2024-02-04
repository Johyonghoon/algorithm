import java.util.*;
import java.io.*;

/**
 * 임의의 순열 오름차순 정렬
 * 입력 받은 k번째 순열을 구할 때는 앞에서부터 몇 번째 숫자인지를 각 자리수마다 (N-i)!로 나눈 몫의 번호 숫자 구하기
 */

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        // (N-1)! 부터 순차 탐색
        long d = 1;
        for (int i = 2; i < N; i++) {
            d *= i;
        }

        st = new StringTokenizer(br.readLine());
        int Q = Integer.parseInt(st.nextToken());
        // 사용 여부 확인
        boolean[] visited = new boolean[N+1];

        if (Q == 1) {  // k 입력 받기 => k번째 순열 구하기
            long[] order = new long[N];
            long k = Long.parseLong(st.nextToken());
            k--;  // 0번째 수열부터 시작한다고 가정
            for (int i = 0; i < N-1; i++) {
                order[i] = k / d;
                k %= d;
                d /= N-i-1;
            }

            for (int i = 0; i < N; i++) {
                long target = order[i];
                long cnt = 0;
                for (int j = 1; j <= N; j++) {
                    if (visited[j]) continue;
                    if (target == cnt) {
                        visited[j] = true;
                        System.out.printf(j + " ");
                        break;
                    }
                    cnt++;
                }
            }
        } else {  // 임의의 순열 N개의 수 입력 받기 => 해당 순열이 몇번째 순열인지 구하기
            int[] numbers = new int[N];
            for (int i = 0; i < N; i++) {
                numbers[i] = Integer.parseInt(st.nextToken());
            }
            long k = 1;

            for (int i = 0; i < N-1; i++) {
                int cnt = 0;
                for (int j = 1; j <= N; j++) {
                    if (visited[j]) continue;
                    if (numbers[i] == j) {
                        visited[j] = true;
                        k += cnt * d;
                        break;
                    }
                    cnt++;
                }
                d /= N-i-1;
            }

            System.out.println(k);
        }
    }
}