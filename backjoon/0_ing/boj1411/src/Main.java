import java.util.*;
import java.io.*;


public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        ArrayList<Integer>[] words = new ArrayList[N];
        for (int i = 0; i < N; i++) {
            String word = br.readLine();
            words[i] = new ArrayList<>();
            int idx = 1;
            int[] charToString = new int[26];
            for (char c : word.toCharArray()) {
                if (charToString[c - 'a'] == 0) {
                    charToString[c - 'a'] = idx;
                    idx++;
                }
                words[i].add(charToString[c - 'a']);
            }

//            System.out.println(words[i].toString());
        }



        int result = 0;
        for (int i = 0; i < N; i++) {
            for (int j = i+1; j < N; j++) {
                for (int k = 0; k < words[i].size(); k++) {
                    if (words[i].get(k) != words[j].get(k)) break;
                    if (k == words[i].size()-1) result++;
                }
            }
        }

        System.out.println(result);
    }
}