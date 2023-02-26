// Baekjoon 1865
// https://www.acmicpc.net/problem/1865

import java.util.*;
import java.io.*;

public class Main {
    static long INF = Integer.MAX_VALUE;
    static class Node{
        final int from, to, cost;
        Node(int f, int t, int c) {
            this.from = f;
            this.to = t;
            this.cost = c;
        }
    }

    public static void main(String[] args) throws IOException {
        int TC = read();
        StringBuilder sb = new StringBuilder();
        while (TC-- > 0) {
            int N, M, W;
            N = read(); // 지점(노드)의 수
            M = read(); // 도로의 개수
            W = read(); // 웜홀의 개수

            List<Node> costs = new ArrayList<>();
            for (int i=0; i<M+W; i++) {
                int s, e, t;
                s = read();
                e = read();
                t = read();

                if (i < M) {    // 도로는 방향이 없음
                    costs.add(new Node(s, e, t));
                    costs.add(new Node(e, s, t));
                } else {    // 웜홀은 방향이 있으며 가중치가 음수임
                    costs.add(new Node(s, e, -t));
                }
            }

            long[] result = new long[N+1];
            Arrays.fill(result, INF); // 모든 결과값을 INF로 초기화

            result[0] = 0;
            result[1] = 0; // 출발지를 1로 가정
            boolean isNegative = false; // 시간이 줄어들면 true, 줄어들지 않으면 false

            while (N-- >= 0) {
                for (int idx=0; idx<costs.size(); idx++) {
                    Node node = costs.get(idx);
                    int from = node.from;
                    int to = node.to;
                    int cost = node.cost;

                    if (result[to] > result[from] + cost) {
                        result[to] = result[from] + cost;
                        if (N == 0) isNegative = true;
                    }
                }
            }
            sb.append((isNegative)?"YES":"NO").append("\n");
        }
        System.out.println(sb);
    }

    static int read() throws IOException{
        int c, n = System.in.read() & 15;
        while ((c = System.in.read()) > 32) n = (n << 3) + (n << 1) + (c & 15);
        if (c == 13) System.in.read();
        return n;
    }
}
