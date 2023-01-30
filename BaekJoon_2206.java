// Baekjoon 2206
// https://www.acmicpc.net/problem/2206

import java.io.*;
import java.util.*;
public class Main {
    static int N, M;
    static boolean[][][] visited;
    static char[][] map;
    static Queue<int[]> queue = new LinkedList<>();
    static int[][] mv_arr = new int[][]{{0, -1}, {0, 1}, {1, 0}, {-1, 0}};

    static void bfs() {
        int answer = 0;
        while (!queue.isEmpty()) {
            answer++;
            int step = queue.size();
            for (int s=0; s<step; s++) {
                int[] state = queue.poll(); // state = {x, y, 벽 파괴 유무(0 or 1)}
                if (state[0] == N - 1 && state[1] == M - 1) {
                    System.out.println(answer);
                    return;
                }
                for (int[] mv : mv_arr) {
                    int nx = state[0] + mv[0];
                    int ny = state[1] + mv[1];
                    if (0 <= nx && nx < N && 0 <= ny && ny < M && !visited[state[2]][nx][ny]) {
                        visited[state[2]][nx][ny] = true;
                        if (map[nx][ny] == '1') {
                            if (state[2] == 0)
                                queue.offer(new int[]{nx, ny, 1});
                        }
                        else {
                            queue.offer(new int[]{nx, ny, state[2]});
                        }
                    }
                }
            }
        }
        System.out.println(-1);
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        map = new char[N][M];
        visited = new boolean[2][N][M];

        for (int n=0; n<N; n++) {
            map[n] = br.readLine().toCharArray();
        }
        br.close();

        queue.offer(new int[]{0, 0, 0});
        visited[0][0][0] = true;
        bfs();
    }
}
