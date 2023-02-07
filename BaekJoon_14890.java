// Baekjoon 14890
// https://www.acmicpc.net/problem/14890

import java.io.*;
import java.util.*;

public class Main {
    static int[][] map;
    static int N, L;
    public static void main(String[] args) throws IOException {
        N = read();
        L = read();
        int answer = 0;

        map = new int[N][N];
        for (int i=0; i<N; i++)
            for (int j=0; j<N; j++)
                map[i][j] = read();

        for (int r=0; r<N; r++) {
            int[] line = new int[N];
            System.arraycopy(map[r], 0, line, 0, N);
            if (solution(line))
                answer++;
        }

        for (int r=0; r<N; r++) {
            int[] line = new int[N];
            for (int c=0; c<N; c++)
                line[c] = map[c][r];
            if (solution(line))
                answer++;
        }

        System.out.println(answer);
    }

    static boolean solution(int[] line) {
        boolean[] checked = new boolean[N];
        for (int idx=1; idx<N; idx++) {
            if (line[idx-1] != line[idx]) {
                if (Math.abs(line[idx-1] - line[idx]) > 1)  // 낮은 칸과 높은 칸의 높이 차이가 1이 아닌 경우
                    return false;
                if (line[idx-1] < line[idx]) {
                    for (int l=0; l<L; l++) {
                        if (idx - l -1 < 0) // 경사로를 놓다가 범위를 벗어나는 경우
                            return false;
                        if (checked[idx - l -1])    // 경사로를 놓은 곳에 또 경사로를 놓는 경우
                            return false;
                        if (line[idx - l -1] != line[idx - 1])  // 낮은 지점의 칸의 높이가 모두 같지 않거나, L개가 연속되지 않은 경우
                            return false;
                        checked[idx - l -1] = true;
                    }
                } else if (line[idx-1] > line[idx]) {
                    for (int l=0; l<L; l++) {
                        if (idx + l >= N) // 경사로를 놓다가 범위를 벗어나는 경우
                            return false;
                        if (line[idx] != line[idx + l])  // 낮은 지점의 칸의 높이가 모두 같지 않거나, L개가 연속되지 않은 경우
                            return false;
                        checked[idx + l] = true;
                    }
                }
            }
        }
        return true;
    }

    static int read() throws IOException{
        int c, n = System.in.read() & 15;
        while ((c = System.in.read()) > 32) n = (n << 3) + (n << 1) + (c & 15);
        if (c == 13) System.in.read();
        return n;
    }
}
