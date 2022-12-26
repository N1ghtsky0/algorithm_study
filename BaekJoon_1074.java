// Baekjoon 1074
// https://www.acmicpc.net/problem/1074

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int r = sc.nextInt();
        int c = sc.nextInt();

        sc.close();

        solution((int) Math.pow(2, N), r, c, 0);
    }

    static void solution(int n, int row, int col, int answer) {
        if (n == 1) {
            System.out.println(answer + 2 * row + col);
            return;
        }

        int s = (n - 1) / 2;

        if (row <= s)
            if (col > s)    // 제1사분면
                solution(n/2, row, col % (n/2), answer + n/2 * n/2);
            else            // 제2사분면
                solution(n/2, row, col, answer);
        else
            if (col <= s)   // 제3사분면
                solution(n/2, row % (n/2), col, answer + n/2 * n/2 * 2);
            else            // 제2사분면
                solution(n/2, row % (n/2), col % (n/2), answer + n/2 * n/2 * 3);
    }
}

