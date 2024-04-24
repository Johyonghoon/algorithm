import java.util.*;
import java.io.*;


public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int i = 0; i < N; i++) {
            int number = Integer.parseInt(br.readLine());
            pq.add(number);
        }

        int result = 0;
        while (pq.size() > 1) {
            int A = pq.poll();
            int B = pq.poll();
            int sum = A + B;
            result += sum;
            pq.add(sum);
        }

        if (N == 1) System.out.println(pq.poll());
        else System.out.println(result);
    }
}