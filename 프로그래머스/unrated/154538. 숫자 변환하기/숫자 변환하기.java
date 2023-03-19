import java.util.*;
class Solution {
    Queue<int[]> queue = new LinkedList<>();
    boolean[] visited;
    public int solution(int x, int y, int n) {
        visited = new boolean[y+1];
        queue.offer(new int[]{x, 0});
        while (!queue.isEmpty()) {
            int[] tmp = queue.poll();
            if (tmp[0] == y) return tmp[1];
            if (tmp[0] + n <= y && !visited[tmp[0] + n]) chk(tmp[0] + n, tmp[1]);
            if (tmp[0] * 2 <= y && !visited[tmp[0] * 2]) chk(tmp[0] * 2, tmp[1]);
            if (tmp[0] * 3 <= y && !visited[tmp[0] * 3]) chk(tmp[0] * 3, tmp[1]);
        }
        return -1;
    }
    void chk(int x, int cnt) {
        queue.offer(new int[]{x, cnt+1});
        visited[x] = true;
    }
}