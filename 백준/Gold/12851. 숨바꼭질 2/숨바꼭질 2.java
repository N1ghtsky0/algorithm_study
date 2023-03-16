import java.util.*;
import java.io.*;
public class Main {
    static class Node {
        final int X;
        final int cnt;

        Node(int x, int c) {
            this.X = x;
            this.cnt = c;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        br.close();
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int answer = 0;
        int min_time = Integer.MAX_VALUE;
        if (K <= N) {
            answer = 1;
            min_time = N - K;
        } else {
            int[] counts = new int[200001];
            Arrays.fill(counts, -1);
            Queue<Node> queue = new LinkedList<>();
            queue.offer(new Node(N, 0));
            Node node;
            int x, cnt;
            while (!queue.isEmpty()) {
                node = queue.poll();
                x = node.X;
                cnt = node.cnt;

                if (cnt > min_time) break;
                for (int nx : new int[]{x - 1, x + 1, x * 2}) {
                    if (nx == K && cnt + 1 <= min_time) {
                        min_time = cnt + 1;
                        answer++;
                    }
                    if (0 <= nx && nx <= 200000 && ((counts[nx]==-1) || (counts[nx] >= cnt + 1))) {
                        counts[nx] = cnt + 1;
                        queue.offer(new Node(nx, cnt+1));
                    }
                }
            }
        }
        System.out.println(min_time);
        System.out.println(answer);
    }
}