import java.util.*;
class Solution {
    final int[] dx = {-1, 0, 1, 0};
    final int[] dy = {0, -1, 0, 1};
    
    public int solution(String[] maps) {
        int startX = 0;
        int startY = 0;
        
        for (int r = 0; r < maps.length; r++) {
            for (int c = 0; c < maps[r].length(); c++) {
                if ('S' == maps[r].charAt(c)) {
                    startX = c;
                    startY = r;
                    break;
                }
            }
        }
        
        int[] distanceToLever = findShortestDistance(maps, startX, startY, 'L');
        if (distanceToLever == null) { return -1; }
        int[] distanceToExit = findShortestDistance(maps, distanceToLever[1], distanceToLever[0], 'E');
        if (distanceToExit == null) { return -1; }
        return distanceToLever[2] + distanceToExit[2];
    }
    
    private int[] findShortestDistance(String[] maps, int startX, int startY , char target) {
        int maxX = maps[0].length();
        int maxY = maps.length;
        boolean[][] visited = new boolean[maxY][maxX];
        
        Queue<int[]> steps = new LinkedList<>();
        steps.add(new int[]{startY, startX, 0});
        while (!steps.isEmpty()) {
            int[] step = steps.poll();
            int nextStep = ++step[2];
            for (int d = 0; d < 4; d++) {
                int y = step[0] + dy[d];
                int x = step[1] + dx[d];
                if (0 <= y && y < maxY && 0 <= x && x < maxX && 'X' != maps[y].charAt(x) && !visited[y][x]) {
                    steps.add(new int[]{y, x, nextStep});
                    visited[y][x] = true;
                    if (target == maps[y].charAt(x)) {
                        return new int[]{y, x, nextStep};
                    }
                }
            }
        }
        return null;
    }
}