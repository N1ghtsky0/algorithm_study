// Baekjoon 7576
// https://www.acmicpc.net/problem/7576

import java.io.*;
import java.util.*;
public class Main {
    static boolean check_right_index(int row, int col, int n, int m) {
        return ((row >= 0) && (row < m)) && ((col >= 0) && (col < n));
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int answer = -1;

        int[] drow = new int[]{-1, 1, 0, 0};
        int[] dcol = new int[]{0, 0, -1, 1};

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[][] tomato_field = new int[M][N];
        Queue<int[]> queue = new LinkedList<>();

        for (int i=0; i<M; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j=0; j<N; j++) {
                int state = Integer.parseInt(st.nextToken());
                tomato_field[i][j] = state;
                if (state == 1)
                    queue.offer(new int[]{i, j});
            }
        }
        br.close();

        while (!queue.isEmpty()) {
            int repeat_num = queue.size();
            for (int num=0; num<repeat_num; num++) {
                int[] coord = queue.poll();
                int row = coord[0];
                int col = coord[1];

                for (int idx=0; idx<4; idx++) {
                    int nrow = row + drow[idx];
                    int ncol = col + dcol[idx];

                    if (check_right_index(nrow, ncol, N, M) && tomato_field[nrow][ncol] == 0) {
                        tomato_field[nrow][ncol] = 1;
                        queue.offer(new int[]{nrow, ncol});
                    }
                }
            }
            answer++;
        }

        for (int r=0; r<M; r++)
            for (int c=0; c<N; c++)
                if (tomato_field[r][c] == 0) {
                    System.out.println(-1);
                    return;
                }
        System.out.println(answer);
    }
}
