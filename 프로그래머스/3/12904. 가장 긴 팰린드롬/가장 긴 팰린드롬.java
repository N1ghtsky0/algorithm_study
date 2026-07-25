class Solution
{
    public int solution(String s)
    {
        int answer = 0;
        
        for (int idx=0; idx < s.length(); idx++) {
            int oddLen = check(s, idx, idx);
            int evenLen = check(s, idx, idx + 1);
            
            answer = Math.max(answer, Math.max(oddLen, evenLen));
        }

        return answer;
    }
    
    private int check(String s, int left, int right) {
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        return right - left - 1;
    }
}