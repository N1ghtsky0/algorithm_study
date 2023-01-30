// Baekjoon 1991
// https://www.acmicpc.net/problem/1991

import java.io.*;
import java.util.*;

public class Main {
    static HashMap<String, String[]> tree = new HashMap<>();

    static void front(String p) {
        if (p.equals("."))
            return;
        System.out.print(p);
        front(tree.get(p)[0]);
        front(tree.get(p)[1]);
    }

    static void middle(String p) {
        if (p.equals("."))
            return;
        middle(tree.get(p)[0]);
        System.out.print(p);
        middle(tree.get(p)[1]);
    }

    static void back(String p) {
        if (p.equals("."))
            return;
        back(tree.get(p)[0]);
        back(tree.get(p)[1]);
        System.out.print(p);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        for (int n=0; n<N; n++) {
            String[] input = br.readLine().split(" ");
            tree.put(input[0], new String[]{input[1], input[2]});
        }
        br.close();

        front("A");
        System.out.println();
        middle("A");
        System.out.println();
        back("A");
    }
}
