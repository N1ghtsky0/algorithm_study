import java.util.*;
class Solution {
    public int solution(String s) {
        int answer = 0;
        int x = 0, x_ = 0;
        char t = ' ';
        for (int idx=0; idx<s.length(); idx++) {
            if (x == 0) {
                t = s.charAt(idx);
                x++;
                continue;
            }
            char t_ = s.charAt(idx);

            if (t == t_) x++;
            else x_++;

            if (x == x_) {
                answer++;
                x = 0;
                x_ = 0;
            }
        }
        answer += (x>0)?1:0;
        return answer;
    }
}