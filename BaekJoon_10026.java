// Baekjoon 10026
// https://www.acmicpc.net/problem/10026

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        String[][] image = new String[N][N];
        String[][] color_weak = new String[N][N];

        for (int n=0; n<N; n++) {
            image[n] = br.readLine().split("");
            color_weak[n] = image[n].clone();
            for (int m=0; m<N; m++)
                if (color_weak[n][m].equals("G"))
                    color_weak[n][m] = "R";
        }

        br.close();

        System.out.print(BFS(N, image));
        System.out.print(" ");
        System.out.print(BFS(N, color_weak));
    }

    static int BFS(int N, String[][] img) {
        int answer = 0;

        for (int r=0; r<N; r++)
            for (int c=0; c<N; c++) {
                if (!img[r][c].equals("N")) {
                    String target = img[r][c];
                    List<int[]> bfs = new ArrayList<>();
                    bfs.add(new int[]{r, c});

                    while (bfs.size() != 0) {
                        int[] state;
                        state = bfs.get(0);
                        bfs.remove(0);

                        List<int[]> tmp = new ArrayList<>();
                        tmp.add(new int[]{Math.max(0, state[0]-1), state[1]});
                        tmp.add(new int[]{Math.min(state[0]+1, N-1), state[1]});
                        tmp.add(new int[]{state[0], Math.max(0, state[1]-1)});
                        tmp.add(new int[]{state[0], Math.min(state[1]+1, N-1)});

                        for (int[] next: tmp) {
                            if (img[next[0]][next[1]].equals(target)) {
                                bfs.add(new int[]{next[0], next[1]});
                                img[next[0]][next[1]] = "N";
                            }
                        }
                    }
                    answer++;
                }
            }
        return answer;
    }
}
