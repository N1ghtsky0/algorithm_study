import java.util.*;
import java.io.*;
public class Main {
    static class Node {
        final int X;
        final int cnt;
        final String path;

        Node(int x, int c, String p) {
            this.X = x;
            this.cnt = c;
            this.path = p;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        br.close();
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        if (K <= N) {
            System.out.println(N - K);
            for (int n=N; n>=K; n--)
                System.out.print(n+" ");
        } else {
            boolean[] visited = new boolean[200001];
            Queue<Node> queue = new LinkedList<>();
            queue.offer(new Node(N, 0, String.valueOf(N)));
            Node node;
            int x, cnt;
            String p;
            while (!queue.isEmpty()) {
                node = queue.poll();
                x = node.X;
                cnt = node.cnt;
                p = node.path;
                if (x == K) {
                    System.out.println(cnt);
                    System.out.println(p);
                    return;
                }

                for (int nx : new int[]{x - 1, x + 1, x * 2}) {
                    if (0 <= nx && nx <= 200000 && !visited[nx]) {
                        visited[nx] = true;
                        queue.offer(new Node(nx, cnt+1, p + " " + nx));
                    }
                }
            }
        }
    }
}