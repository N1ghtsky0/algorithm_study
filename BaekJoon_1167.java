// Baekjoon 1167
// https://www.acmicpc.net/problem/1167

import java.util.*;
import java.io.*;
public class Main {
    static List<List<int[]>> tree = new ArrayList<>();
    static boolean[] visited;
    static int answer = 0;
    public static void main(String[] args) throws IOException{
        int V = read();
        visited = new boolean[V+1];
        for (int v=0; v<=V; v++)
            tree.add(new ArrayList<>());
        for (int v=1; v<=V; v++) {
            int parent = read();
            while (true) {
                int child = read();
                if (child == -1) break;
                int dist = read();
                tree.get(parent).add(new int[]{child, dist});
            }
        }
        visited[1] = true;
        dfs(1);
        System.out.println(answer);
    }

    static int dfs(int p) {
        List<Integer> tmp = new ArrayList<>();
        tmp.add(0);
        for (int[] child : tree.get(p)) {
            if (!visited[child[0]]) {
                visited[child[0]] = true;
                tmp.add(child[1] + dfs(child[0]));
            }
        }
        tmp.sort(Comparator.reverseOrder());
        if (tmp.get(0) == 0) return 0;
        if (tmp.get(0) + tmp.get(1) > answer) answer = tmp.get(0) + tmp.get(1);
        return tmp.get(0);
    }

    static int read() throws IOException{
        int c, n = System.in.read() & 15;
        boolean isNegative = n == 13;
        if (isNegative) n = System.in.read() & 15;
        while ((c = System.in.read()) > 32) n = (n << 3) + (n << 1) + (c & 15);
        if (c == 13) System.in.read();
        return isNegative?~n + 1:n;
    }
}
