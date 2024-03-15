class Solution {
    public int solution(int n, int t) {
        int answer = n;
        for (; t>0; t--) {
            answer = 2 * answer;
        }
        return answer;
    }
}