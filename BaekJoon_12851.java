// Baekjoon 12851
// https://www.acmicpc.net/problem/12851

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
        if (K <= N) {    // 수빈이의 위치가 동생과 같거나 뒤에 있을 경우 -1로 계속 이동하는 것이 최선의 방법
            answer = 1;
            min_time = N - K;
        } else {
            int[] counts = new int[200001];    // 100000을 넘어서 -1로 이동했을 때 가정
            Arrays.fill(counts, -1);
            Queue<Node> queue = new LinkedList<>();
            queue.offer(new Node(N, 0));    // 수빈이의 출발위치에서의 이동 횟수는 0
            Node node;
            int x, cnt;
            while (!queue.isEmpty()) {
                node = queue.poll();
                x = node.X;
                cnt = node.cnt;

                if (cnt > min_time) break;    // cnt가 최소 이동횟수를 넘을 경우 이후는 모두 최소 이동횟수보다 큰 값이므로 탈출
                for (int nx : new int[]{x - 1, x + 1, x * 2}) {
                    if (nx == K && cnt + 1 <= min_time) {    // 1초 후의 위치가 최소 이동횟수보다 작거나 같다면 방법의 수에 +1
                        min_time = cnt + 1;
                        answer++;
                    }
                    if (0 <= nx && nx <= 200000 && ((counts[nx]==-1) || (counts[nx] >= cnt + 1))) {    // 이미 방문했던 지점이라도 이동 횟수가 작거나 같을 경우 queue에 다시 추가
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
