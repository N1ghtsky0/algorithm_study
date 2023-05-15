import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        int N = read();
        int[][] map = new int[N][N];
        for (int n=0; n<N; n++)
            for (int c=0; c<N; c++)
                map[n][c] = read();

        int[][] dp = new int[N][N];
        dp[0][1] = 1;
        ArrayDeque<int[]> arraydeque = new ArrayDeque<>();
        arraydeque.offer(new int[]{0, 1, 0});    // {x, y, d}, (d: 방향 {0: 가로, 1: 세로, 2: 대각선})

        while (!arraydeque.isEmpty()) {
            int[] state = arraydeque.poll();
            int r, c, d;
            r = state[0];
            c = state[1];
            d = state[2];
            boolean[] d_ = new boolean[]{true, true, true};
            if (d != 2) d_[1-d] = false;    // 가로 세로 교차 불가 >> 가로로 이동해온 경우 세로로 이동 불가, 반대도 동일

            if (d_[0]) {
                if (c + 1 < N && map[r][c+1] == 0) {    // 가로로 이동가능 할때
                    arraydeque.offer(new int[]{r, c+1, 0});
                    dp[r][c+1] += 1;
                }
            }

            if (d_[1]) {
                if (r + 1 < N && map[r+1][c] == 0) {    // 세로로 이동가능 할때
                    arraydeque.offer(new int[]{r+1, c, 1});
                    dp[r+1][c] += 1;
                }
            }

            if (d_[2]) {
                if (r + 1 < N && c + 1 < N && map[r+1][c] == 0 && map[r+1][c+1] == 0 && map[r][c+1] == 0) {  // 대각선으로 이동가능 할때
                    arraydeque.offer(new int[]{r+1, c+1, 2});
                    dp[r+1][c+1] += 1;
                }
            }
        }
        System.out.println(dp[N-1][N-1]);
    }

    static int read() throws IOException{
        int c, n = System.in.read() & 15;
        while ((c = System.in.read()) > 32) n = (n << 3) + (n << 1) + (c & 15);
        if (c == 13) System.in.read();
        return n;
    }
}