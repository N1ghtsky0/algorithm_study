class Solution {
    public String solution(String s, String skip, int index) {
        StringBuilder answerBuilder = new StringBuilder();
        char[] skipArr = skip.toCharArray();
        for (char c : s.toCharArray()) {
            answerBuilder.append(skipChar(c, skipArr, index));
        }
        return answerBuilder.toString();
    }
    
    private char skipChar(char c, char[] skipArr, int index) {
            while (index > 0) {
                boolean isSkip = false;
                char _c = (c == 'z') ? 'a' : (char) (c + 1);
                for (char _skip : skipArr) {
                    if (_c == _skip) {
                        isSkip = true;
                        break;
                    }
                }
                c = _c;
                if (!isSkip) {
                    index--;
                }
            }
            return c;
        }
}