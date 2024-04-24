import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int H = Integer.parseInt(st.nextToken());
        int W = Integer.parseInt(st.nextToken());
        int X = Integer.parseInt(st.nextToken());
        int Y = Integer.parseInt(st.nextToken());

        int[][] graph = new int[H+X][W+Y];
        for (int y = 0; y < H + X; y++) {
            st = new StringTokenizer(br.readLine());
            for (int x = 0; x < W + Y; x++) {
                graph[y][x] = Integer.parseInt(st.nextToken());
            }
        }

        int[][] og = new int[H][W];
        for (int y = 0; y < H; y++) {
            for (int x = 0; x < W; x++) {
                og[y][x] = graph[y][x];
                graph[y+X][x+Y] -= og[y][x];
            }
        }

        for (int y = 0; y < H; y++) {
            for (int x = 0; x < W; x++) {
                System.out.print(og[y][x] + " ");
            }
            System.out.println();
        }

    }
}