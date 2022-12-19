// Baekjoon 11724
// https://www.acmicpc.net/problem/11724

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;

public class Main {
    public static void main(String[] args) throws IOException {
        int answer = 0;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] NM = br.readLine().split(" ");
        int N = Integer.parseInt(NM[0]);
        int M = Integer.parseInt(NM[1]);

        HashMap<Integer, ArrayList<Integer>> map = new HashMap<>();

        for (int i=1; i <= N; i++) {
            map.put(i, new ArrayList<>());
        }

        for (int i=0; i < M; i++) {
            String[] uv = br.readLine().split(" ");
            int u = Integer.parseInt(uv[0]);
            int v = Integer.parseInt(uv[1]);
            map.get(u).add(v);
            map.get(v).add(u);
        }

        int[] check_list = new int[N];

        for (int i=1; i <= N; i++) {
            if (check_list[i-1] == 0) {
                DFS(i, map, check_list);
                answer += 1;
            }
        }

        System.out.println(answer);
        br.close();
    }

    static void DFS(int node, HashMap<Integer, ArrayList<Integer>> map, int[] chk_lst) {
        for (Integer i : map.get(node)) {
            if (chk_lst[i-1] == 0) {
                chk_lst[i-1] = 1;
                DFS(i, map, chk_lst);
            }
        }
    }
}
