// Baekjoon 14503
// https://www.acmicpc.net/problem/14503

import java.io.*;
import java.util.*;
public class Main {
    static int N, M, r, c, d;
    static int[][] MAP;
    static int[] dx = new int[]{-1, 0, 1, 0};
    static int[] dy = new int[]{0, 1, 0, -1};
    public static void main(String[] args) throws IOException {
        init();
        int answer = 1;
        while (true) {
            int r_, c_;
            boolean forElse = true;
            for (int mv_idx=0; mv_idx<4; mv_idx++) {
                d = (d>0)?d-1:3;
                r_ = r + dx[d];
                c_ = c + dy[d];
                if (MAP[r_][c_] == 0) {
                    r = r_;
                    c = c_;
                    MAP[r][c] = 2;
                    answer++;
                    forElse = false;
                    break;
                }
            }
            if (forElse) {
                r_ = r + dx[(d>1)?d-2:((d>0)?3:2)];
                c_ = c + dy[(d>1)?d-2:((d>0)?3:2)];
                if (MAP[r_][c_] == 1)
                    break;
                else {
                    r = r_;
                    c = c_;
                }
            }
        }
        System.out.println(answer);
    }

    static void init() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        MAP = new int[N][M];

        st = new StringTokenizer(br.readLine());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        d = Integer.parseInt(st.nextToken());

        for (int n=0; n<N; n++) {
            st = new StringTokenizer(br.readLine());
            for (int m = 0; m < M; m++)
                MAP[n][m] = Integer.parseInt(st.nextToken());
        }
        br.close();
        MAP[r][c] = 2;
    }
}
