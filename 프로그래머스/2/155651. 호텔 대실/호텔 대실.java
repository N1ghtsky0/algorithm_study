import java.util.Arrays;
class Solution {
    public int solution(String[][] bookTimes) {
        int[] timeTable = new int[24 * 60];
        
        for (String[] bookTime: bookTimes) {
            int startTime = timeToMinute(bookTime[0]);
            int endTime = Math.min(timeToMinute(bookTime[1]) + 9, 24 * 60 - 1);
            for (int t=startTime; t<=endTime; t++) {
                timeTable[t] += 1;
            }
        }
        return Arrays.stream(timeTable).max().getAsInt();
    }
    
    private int timeToMinute(String time) {
        int hour = Integer.valueOf(time.split(":")[0]);
        int minute = Integer.valueOf(time.split(":")[1]);
        return hour * 60 + minute;
    }
}