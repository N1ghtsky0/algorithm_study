import java.util.*;

class Solution {
    public int solution(int n, int[][] edge) {
        int answer = 0;
        
        Map<Integer, List<Integer>> connectionMap = new HashMap<>();
        for (int[] conn: edge) {
            connectionMap.computeIfAbsent(conn[0], k -> new ArrayList()).add(conn[1]);
            connectionMap.computeIfAbsent(conn[1], k -> new ArrayList()).add(conn[0]);
        }
        
        Set<Integer> visited = new HashSet<>();
        visited.add(1);
        Queue<Integer> queue = new LinkedList();
        queue.add(1);
        while (!queue.isEmpty()) {
            answer = queue.size();
            for (int i=0; i < answer; i++) {
                int current = queue.poll();
                for (int next: connectionMap.get(current)) {
                    if (visited.add(next)) {
                        queue.add(next);
                    }
                }
            }
        }
        
        return answer;
    }
}