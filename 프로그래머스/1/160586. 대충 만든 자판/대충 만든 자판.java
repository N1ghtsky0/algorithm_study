class Solution {
    public int[] solution(String[] keymap, String[] targets) {
        int[] answer = new int[targets.length];
        int[] minClickToCreateChar = new int[26];
        for (String key : keymap) {
            int idx = 1;
            for (char c : key.toCharArray()) {
                int charIdx = c - 'A' + 0;
                if (minClickToCreateChar[charIdx] == 0) {
                    minClickToCreateChar[charIdx] = idx;
                } else {
                    minClickToCreateChar[charIdx] = minClickToCreateChar[charIdx] < idx ? minClickToCreateChar[charIdx] : idx;
                }
                idx++;
            }
        }
        
        int answerIdx = 0;
        for (String target: targets) {
            int count = 0;
            for (char targetChar: target.toCharArray()) {
                int cnt = minClickToCreateChar[targetChar - 'A' + 0];
                if (cnt == 0) {
                    count = -1;
                    break;
                }
                count += cnt;
            }
            answer[answerIdx] = count;
            answerIdx++;
        }
        return answer;
    }
}