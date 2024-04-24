import java.util.*;
import java.io.*;

/*
숫자는 0 또는 1이므로, 왼쪽 상단부터 출발한다면 (0, 0) 위치의 숫자는
(0, 0) 위치를 가장 왼쪽 상단으로 가지는 3 * 3 으로만 숫자를 바꿀 수 있다.
바로 오른쪽 좌표 (0, 1)의 경우 (0, 0)에 의해 바뀌거나 (0, 1)에 의해 바뀐다.
따라서 (0, 0)에 의해 바뀐 후 (0, 1)이 다를 경우 (0, 1)을 바꿔야만 가능하다.
모든 좌표를 순서대로 탐색하면 자기 자신에 영향을 미치는 3*3 사갹형은 미리 결정되므로
자기 자신의 경우만 고려한 후 전체를 탐색하여 틀리다면 불가능하다.
 */

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[][] graph = new int[N][M];

        for (int y = 0; y < N; y++) {
            int[] numbers = new int[M];
            String numberString = br.readLine();

            for (int x = 0; x < M; x++) {
                graph[y][x] = Character.getNumericValue(numberString.charAt(x));
            }
        }

        int[][] target = new int[N][M];

        for (int y = 0; y < N; y++) {
            int[] numbers = new int[M];
            String numberString = br.readLine();

            for (int x = 0; x < M; x++) {
                target[y][x] = Character.getNumericValue(numberString.charAt(x));
            }
        }

        int result = 0;

        for (int y = 0; y <= N-3; y++) {
            for (int x = 0; x <= M-3; x++) {
                if (graph[y][x] != target[y][x]) {
                    result++;
                    for (int ny = 0; ny < 3; ny++) {
                        for (int nx = 0; nx < 3; nx++) {
                            graph[y + ny][x + nx] = 1 - graph[y + ny][x + nx];
                        }
                    }
                }
            }
        }

        boolean isTrue = true;
        for (int y = 0; y < N; y++) {
            for (int x = 0; x < M; x++) {
                if (graph[y][x] != target[y][x]) {
                    isTrue = false;
                    break;
                }
            }
            if (!isTrue) break;
        }

        if (isTrue) System.out.println(result);
        else System.out.println(-1);

    }
}