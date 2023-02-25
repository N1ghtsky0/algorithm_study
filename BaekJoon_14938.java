// Baekjoon 14938
// https://www.acmicpc.net/problem/14938

import java.util.*;
import java.io.*;
public class Main {
    static int INF = 1000000000;

    public static void main(String[] args) throws IOException {
        int N = read();
        int M = read();
        int R = read();

        int[] items = new int[N+1];
        int[][] costs = new int[N+1][N+1];
        for (int[] cost: costs) Arrays.fill(cost, INF);

        for (int i=1; i<=N; i++) {
            costs[i][i] = 0;
            items[i] = read();
        }

        for (int r=0; r<R; r++) {
            int s, e, t;
            s = read();
            e = read();
            t = read();

            if (costs[s][e] > t) {
                costs[s][e] = t;
                costs[e][s] = t;
            }
        }

        for (int k=1; k<=N; k++) {
            for (int i=1; i<=N; i++) {
                for (int j=1; j<=N; j++) {
                    if (costs[i][j] > costs[i][k] + costs[k][j]) costs[i][j] = costs[i][k] + costs[k][j];
                }
            }
        }
        int answer = 0;
        for (int row=1; row<=N; row++) {
            int answer_ = 0;
            for (int col=1; col<=N; col++) {
                if (costs[row][col] <= M) answer_ += items[col];
            }
            if (answer < answer_) answer = answer_;
        }

        System.out.println(answer);
    }

    static int read() throws IOException{
        int c, n = System.in.read() & 15;
        while((c = System.in.read()) > 32) n = (n << 3) + (n << 1) + (c & 15);
        if (c == 13) System.in.read();
        return n;
    }
}
