package boj17406;

import java.util.*;
import java.io.*;

public class Solution {
	
	static int N;
	static int M;
	static int K;
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		
		// 그래프 그리기
		int[][] graph = new int[N][M];
		for (int y=0; y<N; y++) {
			st = new StringTokenizer(br.readLine());
			for (int x=0; x<M; x++) {
				graph[y][x] = Integer.parseInt(st.nextToken());
			}
		}
		
		// 연산 입력 받기
		int[][] OP = new int[6][3];
		for (int y=0; y<K; y++) {
			st = new StringTokenizer(br.readLine());
			for (int x=0; x<M; x++) {
				OP[y][x] = Integer.parseInt(st.nextToken());
			}
		}
		
		
		
	}
	
	// 회전 연산 만들기, 시계방향 회전
	static int[][] rotate(int[][] graph, int[] op) {
		int[][] newGraph = graph.clone();
		int ny = op[0]-1;
		int nx = op[1]-1;
		int s = op[2];
		
		for (int radius=1; radius<=s; radius++) {
			// ey = ny - s일 때
			for (int dx=-s+1; dx<=s; dx++) {
				newGraph[ny-s][nx+dx] = graph[ny-s][nx+dx-1];
			}
			// ey = ny +_s일 때
			for (int dx=s-1; dx>= -s; dx--) {
				newGraph[ny+s][nx+dx] = graph[ny+s][nx+dx+1];
			}
			// ex = nx - s일 때
			for (int dy=-s+1; dy<=s; dy++) {
				newGraph[ny+dy][nx-s] = graph[ny+dy-1][nx-s];
			}
			// ex = nx + s일 때
			for (int dy=s-1; dy>= -s; dy--) {
				newGraph[ny+dy][nx+s] = graph[ny+dy+1][nx+s];
			}
		}

		printMatrix(graph);
		printMatrix(newGraph);
		
		return newGraph;
	}
	
	static void printMatrix(int[][] graph) {
		StringBuilder sb = new StringBuilder();
		for (int y=0; y<N; y++) {
			for (int x=0; x<M; x++) {
				sb.append(graph[y][x]);
			}
			sb.append('\n');
		}
		
		System.out.println(sb);
	}
}
