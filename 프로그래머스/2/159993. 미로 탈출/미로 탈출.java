import java.util.*;
class Solution {
    final int[] dx = {-1, 0, 1, 0};
    final int[] dy = {0, -1, 0, 1};
    
    public int solution(String[] maps) {
        int maxX = maps[0].length();
        int maxY = maps.length;
        boolean[][] visited = new boolean[maxY][maxX];
        
        Queue<int[]> steps = new LinkedList<>();
        int answer = -1;
        //1. 시작지점 찾기
        for (int r = 0; r < maps.length; r++) {
            for (int c = 0; c < maps[r].length(); c++) {
                if ('S' == maps[r].charAt(c)) {
                    visited[r][c] = true;
                    steps.offer(new int[]{r, c, 0});
                    break;
                }
            }
        }
        
        //2. 레버까지 최단거리 찾기
        boolean findLever = false;
        while (!findLever && !steps.isEmpty()) {
            int[] step = steps.poll();
            int nextStep = ++step[2];
            for (int d = 0; d < 4; d++) {
                int y = step[0] + dy[d];
                int x = step[1] + dx[d];
                if (0 <= y && y < maxY && 0 <= x && x < maxX && 'X' != maps[y].charAt(x) && !visited[y][x]) {
                    steps.offer(new int[]{y, x, nextStep});
                    visited[y][x] = true;
                    if ('L' == maps[y].charAt(x)) {
                        findLever = true;
                        answer = nextStep;
                        steps.clear();
                        steps.offer(new int[]{y, x, 0});
                        visited = new boolean[maxY][maxX];
                        break;
                    }
                }
            }
        }
        
        if (!findLever) { return -1; }
        
        //3. 레버부터 출구까지 최단거리 찾기
        boolean findExit = false;
        while (!findExit && !steps.isEmpty()) {
            int[] step = steps.poll();
            int nextStep = ++step[2];
            for (int d = 0; d < 4; d++) {
                int y = step[0] + dy[d];
                int x = step[1] + dx[d];
                if (0 <= y && y < maxY && 0 <= x && x < maxX && 'X' != maps[y].charAt(x) && !visited[y][x]) {
                    steps.offer(new int[]{y, x, nextStep});
                    visited[y][x] = true;
                    if ('E' == maps[y].charAt(x)) {
                        findExit = true;
                        answer += nextStep;
                        break;
                    }
                }
            }
        }
        
        if (!findExit) { return -1; }
        return answer;
    }
}