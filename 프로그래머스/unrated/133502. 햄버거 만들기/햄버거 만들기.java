import java.util.*;
class Solution {
    public int solution(int[] ingredient) {
        int answer = 0;
        Stack<Integer> stack = new Stack<>();
        for (int i : ingredient) {
            stack.push(i);
            if (i == 1 && stack.size() >= 4) {
                if (takeOut(stack)) {
                    for (int j=0; j<4; j++) {
                        stack.pop();
                    }
                    answer++;
                }
            }
        }
        return answer;
    }

    boolean takeOut(Stack<Integer> stack) {
        int[] hamburger = new int[]{1, 2, 3, 1};
        for (int i=0; i<4; i++) {
            if (stack.get(stack.size() - 4 + i) != hamburger[i])
                return false;
        }
        return true;
    }
}