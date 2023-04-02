import java.io.*;
import java.util.*;
public class Main {

    static Queue<Node> fQueue = new LinkedList<>();
    static Queue<Node> jQueue = new LinkedList<>();
    static boolean[][] visited;
    static int R, C;
    static char[][] MAP;
    static int[][] states;
    static final int INIT_VALUE = Integer.MAX_VALUE;

    static int[] dr = new int[]{-1, 1, 0, 0};
    static int[] dc = new int[]{0, 0, -1, 1};

    static class Node {
        int row, col, cnt;
        Node(int r, int c, int t) {
            this.row = r;
            this.col = c;
            this.cnt = t;
        }
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        MAP = new char[R][C];
        states = new int[R][C];
        visited = new boolean[R][C];

        for (int r=0; r<R; r++) {
            Arrays.fill(states[r], INIT_VALUE);
            MAP[r] = br.readLine().toCharArray();
        }

        br.close();

        init();

        while (!fQueue.isEmpty()) {
            Node fCur = fQueue.poll();
            for (int mv_idx=0; mv_idx<4; mv_idx++) {
                int nr = fCur.row + dr[mv_idx];
                int nc = fCur.col + dc[mv_idx];
                if (0<=nr&&nr<R && 0<=nc&&nc<C && states[nr][nc]==INIT_VALUE) {
                    states[nr][nc] = fCur.cnt + 1;
                    fQueue.offer(new Node(nr, nc, fCur.cnt + 1));
                }
            }
        }

        boolean done = false;
        int answer = 1;
        Node tmp = jQueue.peek();
        if (tmp.row == 0 || tmp.row == R-1 || tmp.col == 0 || tmp.col == C-1)
            done = true;
        while (!jQueue.isEmpty() && !done) {
            Node jCur = jQueue.poll();
            for (int mv_idx=0; mv_idx<4; mv_idx++) {
                int nr = jCur.row + dr[mv_idx];
                int nc = jCur.col + dc[mv_idx];
                if (0<=nr&&nr<R && 0<=nc&&nc<C && !visited[nr][nc]) {
                    visited[nr][nc] = true;
                    if (jCur.cnt + 1 < states[nr][nc]) {
                        if (nr == 0 || nr == R-1 || nc == 0 || nc == C-1) {
                            answer = jCur.cnt + 2;
                            done = true;
                            break;
                        }
                        jQueue.offer(new Node(nr, nc, jCur.cnt + 1));
                    }
                }
            }
            if (done)
                break;
        }
        System.out.println((done)?answer:"IMPOSSIBLE");
    }

    static void init() {
        for (int r=0; r<R; r++)
            for (int c=0; c<C; c++) {
                if (MAP[r][c] == '#') {
                    states[r][c] = 0;
                } else if (MAP[r][c] == 'F') {
                    states[r][c] = 0;
                    fQueue.offer(new Node(r, c, 0));
                } else if (MAP[r][c] == 'J') {
                    jQueue.offer(new Node(r, c, 0));
                    visited[r][c] = true;
                }
            }
    }
}