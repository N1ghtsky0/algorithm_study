import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

class Solution {
    public int solution(int[] ropes, int N) {
        Arrays.sort(ropes);
        int answer = -1;

        for (int i=0; i<N; i++)
            answer = Math.max(answer, ropes[i]*(N-i));

        return answer;
    }
}
public class Main {
    public static void main(String[] args) throws IOException {
        Solution sol = new Solution();

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] input = new int[N];

        for (int i=0; i<N; i++)
            input[i] = Integer.parseInt(br.readLine());

        System.out.println(sol.solution(input, N));
        br.close();
    }
}