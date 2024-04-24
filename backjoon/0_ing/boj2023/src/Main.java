import java.io.*;

public class Main {
    static int N;
    static int[] nextNum = {1, 3, 5, 7, 9};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        int[] startNum = {2, 3, 5, 7};

        for (int number : startNum) {
            dfs(1, number);
        }
    }

    static void dfs(int idx, int number) {
        if (idx == N) {
            System.out.println(number);
            return;
        }

        for (int nxt: nextNum) {
            if (isPrimeNum(number * 10 + nxt)) {
                dfs(idx + 1, number * 10 + nxt);
            }
        }
    }

    static boolean isPrimeNum(int number) {
        for (int i = 2; i < Math.sqrt(number)+1; i++) {
            if (number % i == 0) {
                return false;
            }
        }
        return true;
    }
}
