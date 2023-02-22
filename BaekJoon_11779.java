// Baekjoon 11779
// https://www.acmicpc.net/problem/11779

import java.util.*;
import java.io.*;
public class Main {
    static final Long INF = Long.MAX_VALUE;
    static int N, M;
    static boolean[] visited;
    static List<List<INFO>> costs = new ArrayList<>();
    static List<List<Integer>> answer_path = new ArrayList<>();
    static Long[] answer_cost;

    static class INFO {
        final int nextNode;
        final int cost;
        INFO(int nn, int c) {
            this.nextNode = nn;
            this.cost = c;
        }
    }

    static int getIndex() {
        Long value = INF;
        int index = 0;
        for (int idx=1; idx<=N; idx++) {
            if (!visited[idx] && answer_cost[idx] < value) {
                value = answer_cost[idx];
                index = idx;
            }
        }
        return index;
    }

    static void dijkstra(int s) {
        answer_cost[s] = 0L;
        answer_path.get(s).add(s);
        visited[s] = true;

        for (INFO info : costs.get(s)) {
            if (answer_cost[info.nextNode] > info.cost) {
                answer_cost[info.nextNode] = (long) info.cost;
                answer_path.get(info.nextNode).clear();
                for (int nextNode : answer_path.get(s)) answer_path.get(info.nextNode).add(nextNode);
                answer_path.get(info.nextNode).add(info.nextNode);
            }
        }

        for (int i=0; i<N; i++) {
            int currentNode = getIndex();
            visited[currentNode] = true;
            for (INFO info : costs.get(currentNode)) {
                if (answer_cost[info.nextNode] > info.cost + answer_cost[currentNode]) {
                    answer_cost[info.nextNode] = info.cost + answer_cost[currentNode];
                    answer_path.get(info.nextNode).clear();
                    for (int nextNode : answer_path.get(currentNode)) answer_path.get(info.nextNode).add(nextNode);
                    answer_path.get(info.nextNode).add(info.nextNode);
                }
            }
        }
    }
    public static void main(String[] args) throws IOException {
        N = read();
        M = read();

        visited = new boolean[N + 1];
        answer_cost = new Long[N + 1];
        Arrays.fill(answer_cost, INF);
        for (int n=0; n<=N; n++) {
            costs.add(new ArrayList<>());
            answer_path.add(new ArrayList<>());
        }

        for (int m=0; m<M; m++) {
            int s, e, c;
            s = read();
            e = read();
            c = read();
            costs.get(s).add(new INFO(e, c));
        }

        int start, target;
        start = read();
        target = read();
        dijkstra(start);

        StringBuilder sb = new StringBuilder();
        sb.append(answer_cost[target]).append("\n");
        sb.append(answer_path.get(target).size()).append("\n");
        for (int path : answer_path.get(target)) sb.append(path).append(" ");
        System.out.println(sb);
    }

    static int read() throws IOException{
        int c, n = System.in.read() & 15;
        while((c = System.in.read()) > 32) n = (n << 3) + (n << 1) + (c & 15);
        if (c == 13) System.in.read();
        return n;
    }
}
