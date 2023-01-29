// Baekjoon 1380
// https://www.acmicpc.net/problem/1380

import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int scenario = 0;

        while (true) {
            int n = Integer.parseInt(br.readLine());

            if (n == 0) {
                br.close();
                break;
            }

            scenario++;
            String[] girls = new String[n];
            int[] count = new int[n];

            for (int i=0; i<n; i++)
                girls[i] = br.readLine();

            for (int i=0; i<2*n-1; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                count[Integer.parseInt(st.nextToken()) - 1] += 1;
            }

            for (int idx=0; idx<n; idx++)
                if (count[idx] == 1) {
                    System.out.println(scenario + " " + girls[idx]);
                    break;
                }
        }
    }
}
