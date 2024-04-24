import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        Long K = Long.parseLong(st.nextToken());

        Long[] PREFIX = new Long[N+1];

        st = new StringTokenizer(br.readLine());
        PREFIX[0] = 0L;
        for (int i = 1; i <= N; i++) {
            PREFIX[i] = Long.parseLong(st.nextToken());
            PREFIX[i] += PREFIX[i-1];
        }

        // K = PREFIX[j] - PREFIX[i]
        HashMap<Long, Long> dict = new HashMap<>();
        dict.put(0L, 1L);
        Long result = 0L;
        for (int i = 1; i <= N; i++) {
            Long target = PREFIX[i] - K;
            if (dict.containsKey(target)) result += dict.get(target);
            if (dict.containsKey(PREFIX[i])) dict.put(PREFIX[i], dict.get(PREFIX[i])+1L);
            else dict.put(PREFIX[i], 1L);
        }

//        System.out.println(Arrays.toString(PREFIX));
//        System.out.println(dict.toString());
        System.out.println(result);

    }
}