import java.util.*;
class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        int[] answer = new int[photo.length];
        for (int idx=0; idx<photo.length; idx++) {
            List<String> arrays = new ArrayList<>(Arrays.asList(name));
            for (String p: photo[idx])
                if (arrays.contains(p))
                    answer[idx] += yearning[arrays.indexOf(p)];
        }
        return answer;
    }
}