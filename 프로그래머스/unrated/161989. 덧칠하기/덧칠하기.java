class Solution {
    public int solution(int n, int m, int[] section) {
        int answer = 0;
        int p = section[0] - 1;
        for (int s: section) {
            if (p < s) {
                p = s + m - 1;
                answer++;
            }
        }
        return answer;
    }
}