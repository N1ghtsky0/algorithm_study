// Baekjoon 1297
// https://www.acmicpc.net/problem/1297

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double D = sc.nextDouble();
        double H = sc.nextDouble();
        double W = sc.nextDouble();

        sc.close();

        double x = Math.sqrt(D*D / (H*H + W*W));

        System.out.println((int)Math.floor(H*x) + " " + (int)Math.floor(W*x));
    }
}
