// Baekjoon 2193
// https://www.acmicpc.net/problem/status/2193

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public Long solution(int N) {
        List<Long> dp = new ArrayList<>(Arrays.asList(0L, 1L, 1L));

        for (int n=2; n<N; n++)
            dp.add((dp.get(n-1) + dp.get(n)));

        return dp.get(N);
    }
}
public class Main {
    public static void main(String[] args) throws IOException {
        Solution sol = new Solution();

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        System.out.println(sol.solution(N));
    }
}
