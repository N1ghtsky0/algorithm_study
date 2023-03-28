import java.util.*;
class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        for (String babble : babbling) {
            String pre = "";
            int idx = 0;
            int limit = babble.length();
            boolean isBabble = false;
            while (true) {
                if (idx >= limit - 1) {
                    if (idx == limit) isBabble = true;
                    break;
                }

                if (idx <= limit - 3) {
                    if (Arrays.asList(new String[]{"aya", "woo"}).contains(babble.substring(idx, idx+3))) {
                        if (pre.equals(babble.substring(idx, idx+3))) break;
                        pre = babble.substring(idx, idx+3);
                        idx += 3;
                        continue;
                    }
                }
                
                if (idx <= limit - 2) {
                    if (Arrays.asList(new String[]{"ye", "ma"}).contains(babble.substring(idx, idx+2))) {
                        if (pre.equals(babble.substring(idx, idx+2))) break;
                        pre = babble.substring(idx, idx+2);
                        idx += 2;
                    } else {
                        break;
                    }
                }
            }
            if (isBabble) {
                answer++;
            }
        }
        return answer;
    }
}