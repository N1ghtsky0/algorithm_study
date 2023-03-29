import java.util.*;
class Solution {
    public int solution(int n, int[][] wires) {
        int answer = 100;
        List<List<Integer>> tree = new ArrayList<>();
        for (int i=0; i<=n; i++) tree.add(new ArrayList<>());
        for (int[] wire : wires) {
            tree.get(wire[0]).add(wire[1]);
            tree.get(wire[1]).add(wire[0]);
        }
        
        for (int[] wire : wires) {
            int a = bfs(wire[0], wire[1], tree);
            int b = bfs(wire[1], wire[0], tree);
            answer = Math.min(answer, Math.abs(a-b));
        }
        
        return answer;
    }
    
    int bfs(int s, int e, List<List<Integer>> tree) {
        int ans = 1;
        boolean[] visited = new boolean[tree.size()];
        Queue<Integer> queue = new LinkedList<>();
        queue.add(s);
        visited[s] = true;
        while (!queue.isEmpty()) {
            int node = queue.poll();
            for (int next : tree.get(node)) {
                if (!visited[next] && (next != e)) {
                    visited[next] = true;
                    ans++;
                    queue.add(next);
                }
            }
        }
        return ans;
    }
}