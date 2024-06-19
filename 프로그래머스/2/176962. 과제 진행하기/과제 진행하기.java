import java.util.*;
class Solution {
    public String[] solution(String[][] plans) {
        String[] answer = new String[plans.length];
        Stack<String> subStack = new Stack<>();
        Stack<Integer> timeStack = new Stack<>();

        Arrays.sort(plans, (Comparator.comparingInt(o -> time(o[1]))));

        int ans_idx = 0;
        int curTime;
        for (int idx = 0; idx < plans.length; idx++) {
            curTime = time(plans[idx][1]);
            int nextStartTime = (idx != (plans.length - 1))?time(plans[idx+1][1]): 1440;

            subStack.push(plans[idx][0]);
            timeStack.push(Integer.parseInt(plans[idx][2]));

            while (!timeStack.isEmpty() && curTime < nextStartTime) {
                if (curTime + timeStack.peek() <= nextStartTime) {
                    curTime += timeStack.pop();
                    answer[ans_idx] = subStack.pop();
                    ans_idx++;
                } else {
                    timeStack.push(timeStack.pop() - (nextStartTime - curTime));
                    curTime = nextStartTime;
                }
            }
        }

        while (!subStack.isEmpty()) {
            answer[ans_idx] = subStack.pop();
            ans_idx++;
        }
        return answer;
    }
    
    public int time(String t) {
        String[] t_ = t.split(":");
        return Integer.parseInt(t_[0]) * 60 + Integer.parseInt(t_[1]);
    }
}