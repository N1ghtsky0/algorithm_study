// Baekjoon 1182
// https://www.acmicpc.net/problem/1182

import java.io.*;
import java.util.*;

public class Main {
    static int N, S;
    static int[] nums;
    static int answer = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        S = Integer.parseInt(st.nextToken());
        nums = new int[N];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        dfs(0, -1);

        if (S == 0)
            answer--;
        System.out.println(answer);
    }
    static void dfs(int res, int idx) {
        if (res == S)
            answer++;
        if (idx < N)
            for (int idx_=idx+1; idx_<N; idx_++)
                dfs(res + nums[idx_], idx_);
    }
}
