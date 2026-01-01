class Solution {
    public int[] solution(int[] sequence, int k) {
        int[] answer = {};
        int start = 0;
        int end = 0;
        int diff = sequence.length;
        int sum = 0;
        
        for (;end<sequence.length;end++) {
            sum += sequence[end];
            while (sum > k) {
                sum -= sequence[start++];
            }
            if (sum == k && (end-start < diff)) {
                diff = end - start;
                answer = new int[]{start, end};
            }
        }
        return answer;
    }
}