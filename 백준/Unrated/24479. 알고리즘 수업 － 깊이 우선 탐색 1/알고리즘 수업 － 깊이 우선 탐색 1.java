import java.io.IOException;
import java.util.*;
public class Main {
    static int cnt = 0;
    static boolean[] visited;
    static int N, M, R;
    static int[] answer;
    static List<List<Integer>> trunk = new ArrayList<>();
    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        N =read();
        M = read();
        R = read();

        visited = new boolean[N+1];
        answer = new int[N+1];
        for (int n=0; n<=N; n++) trunk.add(new ArrayList<>());
        for (int m=0; m<M; m++) {
            int u = read();
            int v = read();
            trunk.get(u).add(v);
            trunk.get(v).add(u);
        }
        for (int i=1; i<=N; i++) {
            trunk.get(i).sort(Comparator.naturalOrder());
        }
        
        dfs(R);
        for (int i=1; i <=N; i++) sb.append(answer[i]).append("\n");
        System.out.println(sb);
    }

    public static void dfs(int node) {
        if (!visited[node]) {
            cnt++;
            visited[node] = true;
            answer[node] = cnt;
            for (int next : trunk.get(node)) {
                dfs(next);
            }
        }
    }

    public static int read() throws IOException{
        int c, n = System.in.read() & 15;
        while((c = System.in.read()) > 32) n = (n << 3) + (n << 1) + (c & 15);
        if (c == 13) System.in.read();
        return n;
    }
}