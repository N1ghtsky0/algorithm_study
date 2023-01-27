// Baekjoon 16236
// https://www.acmicpc.net/problem/16236

import java.io.*;
import java.util.*;
public class Main {
    static int[] dx = new int[]{-1, 1, 0, 0};
    static int[] dy = new int[]{0, 0, 1, -1};
    static int answer = 0;

    static int[] chooseNextPos(List<int[]> positions) {
        int[][] arr = new int[positions.size()][2];    // 행, 열을 기준으로 정렬하기 위해서 리스트를 2중 배열로 변환
        for (int idx = 0; idx < positions.size(); idx++) {
            arr[idx] = positions.get(idx);
        }
        Arrays.sort(arr, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                if(o1[0] == o2[0]) {
                    return o1[1] - o2[1];
                }else {
                    return o1[0] - o2[0];
                }
            }
        });
        return arr[0];
    }

    static int[] bfs(int n, int[][] map, int shark_size, int[] shark_pos) {
        boolean[][] visited = new boolean[n][n];
        int distance = 0;
        Deque<int[]> deque = new LinkedList<>();
        deque.offer(shark_pos);
        while (!deque.isEmpty()) {
            distance++;
            List<int[]> canEatFish = new ArrayList<>();
            int step = deque.size();
            for (int s=0; s<step; s++) {
                int[] pos = deque.poll();
                for (int mv_idx=0; mv_idx<4; mv_idx++) {
                    int nx = pos[0] + dx[mv_idx];
                    int ny = pos[1] + dy[mv_idx];
                    if ((0 <= nx && nx < n) && (0 <= ny && ny < n) && !visited[nx][ny] && map[nx][ny] <= shark_size) {
                        visited[nx][ny] = true;
                        deque.offer(new int[]{nx, ny});
                        if (0 < map[nx][ny] && map[nx][ny] < shark_size)
                            canEatFish.add(new int[]{nx, ny});
                    }
                }
            }

            if (!canEatFish.isEmpty()) {
                answer += distance;
                return chooseNextPos(canEatFish);
            }
        }
        return new int[]{-1, -1};
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[][] map = new int[N][N];

        int[] shark_pos = new int[2];
        for (int i=0; i<N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j=0; j<N; j++) {
                 map[i][j] = Integer.parseInt(st.nextToken());
                 if (map[i][j] == 9)
                     shark_pos = new int[]{i, j};
            }
        }
        br.close();
        
        map[shark_pos[0]][shark_pos[1]] = 0;

        int shark_size = 2, exp = 0;
        while (true) {
            shark_pos = bfs(N, map, shark_size, shark_pos);
            if (Arrays.equals(shark_pos, new int[]{-1, -1})) {
                break;
            }
            exp++;
            map[shark_pos[0]][shark_pos[1]] = 0;
            if (shark_size == exp) {
                shark_size++;
                exp = 0;
            }
        }
        System.out.println(answer);
    }
}
