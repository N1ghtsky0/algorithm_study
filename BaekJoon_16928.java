// Baekjoon 16928
// https://www.acmicpc.net/problem/16928

import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N, M;
        int answer = 0;
        HashMap<Integer, Integer> ladders = new HashMap<>();
        HashMap<Integer, Integer> snakes = new HashMap<>();
        boolean[] visited = new boolean[101];

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        for (int n=0; n<N; n++) {
            st = new StringTokenizer(br.readLine());
            int ls = Integer.parseInt(st.nextToken());
            int le = Integer.parseInt(st.nextToken());
            ladders.put(ls, le);
        }

        for (int m=0; m<M; m++) {
            st = new StringTokenizer(br.readLine());
            int ss = Integer.parseInt(st.nextToken());
            int se = Integer.parseInt(st.nextToken());
            snakes.put(ss, se);
        }

        Deque<Integer> bfs = new LinkedList<>();
        bfs.offer(1);

        while (true) {
            int repeat_num = bfs.size();
            for (int num=0; num<repeat_num; num++) {
                int state = bfs.poll();
                for (int dice=1; dice<=6; dice++) {
                    int next_state = state + dice;
                    if (ladders.containsKey(next_state))
                        next_state = ladders.get(next_state);
                    else if (snakes.containsKey(next_state))
                        next_state = snakes.get(next_state);

                    if (next_state >= 100) {
                        System.out.println(answer + 1);
                        return;
                    }
                    if (!visited[next_state]) {
                        visited[next_state] = true;
                        bfs.offer(next_state);
                    }
                }
            }
            answer++;
        }
    }
}
