// BaekJoon 1697
// https://www.acmicpc.net/problem/1697

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public int solution(int n, int k) {
        int answer = 0;

        if (n==k) return answer;

        boolean[] checked = new boolean[100001];
        Queue<Integer> queue = new LinkedList<>();
        queue.add(n);

        while (true) {
            int l = queue.size();
            int[] nextStages;
            for (int i=0; i<l; i++) {
                int s = queue.poll();

                nextStages = new int[]{s-1, s+1, s*2};

                for (int nextStage : nextStages)
                    if (0 <= nextStage && nextStage <= 100000)
                        if (!checked[nextStage]) {
                            if (nextStage == k) return answer + 1;

                            checked[nextStage] = true;
                            queue.add(nextStage);
                        }
            }
            answer += 1;
        }
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        Solution sol = new Solution();

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] NK = br.readLine().split(" ");

        System.out.println(sol.solution(Integer.parseInt(NK[0]), Integer.parseInt(NK[1])));
    }
}
