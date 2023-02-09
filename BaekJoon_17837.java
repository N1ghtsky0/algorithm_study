// Baekjoon 17837
// https://www.acmicpc.net/problem/17837

import java.io.*;
import java.util.*;
public class Main {
    static int N, K;
    // map : 체스판의 정보(바닥 색)을 담은 2차원 배열, pieces : i번째 말의 {x, y, 이동 방향}을 담은 2차원 배열
    static int[][] map, pieces;
    // board : 체스판 위에 있는 말들의 정보 ((x, y)칸에 어떤 체스말들이 있는지)
    static List<List<Deque<Integer>>> board;
    static int[] dx = new int[]{0, 0, 0, -1, 1};
    static int[] dy = new int[]{0, 1, -1, 0, 0};
    public static void main(String[] args) throws IOException {
        init();
        for (int ans=1; ans<=1000; ans++) {
            for (int pieceIDX=1; pieceIDX<=K; pieceIDX++) {
                boolean isBlue = false;
                int x, y, d, nx, ny;
                x = pieces[pieceIDX][0];
                y = pieces[pieceIDX][1];
                d = pieces[pieceIDX][2];

                nx = x + dx[d];
                ny = y + dy[d];

                if (0 < nx && nx <= N && 0 < ny && ny <= N) {
                    switch (map[nx][ny]) {
                        case 0:
                            white(pieceIDX, x, y, nx, ny);
                            break;
                        case 1:
                            red(pieceIDX, x, y, nx, ny);
                            break;
                        case 2:
                            isBlue = true;
                            break;
                        default:
                            break;
                    }
                    if (board.get(nx).get(ny).size() >= 4) {
                        System.out.println(ans);
                        return;
                    }
                } else {    // pieceIDX가 이동하려는 방향이 체스판을 벗어나는 경우
                    isBlue = true;
                }

                if (isBlue) {
                    int d_ = (d==1)?2:(d==2)?1:(d==3)?4:3;  // 원래 이동방향 d의 반대 방향인 d_
                    int nx_, ny_;
                    nx_ = x + dx[d_];
                    ny_ = y + dy[d_];

                    if (0 < nx_ && nx_ <= N && 0 < ny_ && ny_ <= N) {
                        switch (map[nx_][ny_]) {
                            case 0:
                                white(pieceIDX, x, y, nx_, ny_);
                                break;
                            case 1:
                                red(pieceIDX, x, y, nx_, ny_);
                                break;
                            default:
                                break;
                        }
                        pieces[pieceIDX][2] = d_;
                        if (board.get(nx_).get(ny_).size() >= 4) {    // pieceIDX번째 말을 이동 후 해당 칸에 4개 이상의 말이 있을 경우 끝
                            System.out.println(ans);
                            return;
                        }
                    } else {
                        pieces[pieceIDX][2] = d_; // 이미 파란 블록을 만났기에 그 자리에서 방향만 바뀜
                    }
                }
            }
        }
        System.out.println(-1);
    }

    static void white(int target, int x, int y, int nx, int ny) {
        Stack<Integer> tmp = new Stack<>();
        while (true) {
            int i = board.get(x).get(y).pollLast(); // (x, y)의 가장 위에 부터 차례대로 tmp로 이동
            tmp.push(i);
            if (i == target)    // 목표인 말이 나올 때까지 반복
                break;
        }

        int t;
        while (!tmp.isEmpty()) { // tmp의 가장 왼쪽부터 차례대로 (nx, ny)에 삽입 > 순서 변화 X
            t = tmp.pop();
            board.get(nx).get(ny).offerLast(t);
            pieces[t][0] = nx;
            pieces[t][1] = ny;
        }
    }

    static void red(int target, int x, int y, int nx, int ny) {
        while (true) {
            int t = board.get(x).get(y).pollLast();
            board.get(nx).get(ny).offerLast(t); // (x, y)의 가장 위에 부터 차례대로 (nx, ny)로 이동 > 순서 반전
            pieces[t][0] = nx;
            pieces[t][1] = ny;
            if (t == target)
                break;
        }
    }

    static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        map = new int[N+1][N+1];
        for (int i=1; i<=N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= N; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        board = new ArrayList<>();    // (N + 1) x (N + 1) 크기의 말의 위치를 나타내는 List 생성 및 초기화 (0행, 0열은 사용 X)
        for (int i=0; i<=N; i++) {
            List<Deque<Integer>> row = new ArrayList<>();
            for (int j=0; j<=N; j++) {
                row.add(new LinkedList<>());
            }
            board.add(row);
        }

        pieces = new int[K+1][2];
        for (int k=1; k<=K; k++) {
            st = new StringTokenizer(br.readLine());
            int a, b, c;
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            c = Integer.parseInt(st.nextToken());
            pieces[k] = new int[]{a, b, c};
            board.get(a).get(b).offer(k);
        }
        br.close();
    }
}
