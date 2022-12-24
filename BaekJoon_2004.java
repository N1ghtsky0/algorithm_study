// Baekjoon 2004
// https://www.acmicpc.net/problem/2004

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int num2 = 0;
        int num5 = 0;

        int n = sc.nextInt();
        int m = sc.nextInt();
        sc.close();

        for (long i=2L, j=5L; i<=n; i*=2L, j*=5L) {
            num2 += n/i - m/i - (n-m)/i;
            num5 += n/j - m/j - (n-m)/j;
        }
        System.out.println(Math.min(num2, num5));
    }
}

