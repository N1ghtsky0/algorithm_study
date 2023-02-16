// Baekjoon 5639
// https://www.acmicpc.net/problem/5639

import java.util.*;
import java.io.*;
public class Main {
    static List<Integer> pre_result = new ArrayList<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input;
        while ((input = br.readLine()) != null) {
            pre_result.add(Integer.parseInt(input));
        }
        int s_idx = 0;
        int e_idx = -1;
        for (int idx=1; idx < pre_result.size(); idx++) {
            if (pre_result.get(idx) > pre_result.get(s_idx)) {
                e_idx = idx;
                break;
            }
        }
        if (e_idx != -1) {
            post_result(s_idx + 1, e_idx, true);
            post_result(e_idx, pre_result.size(), false);
            System.out.println(pre_result.get(e_idx));
        } else {
            post_result(s_idx+1, pre_result.size(), true);;
        }
        System.out.println(pre_result.get(0));
    }

    static void post_result(int s_idx, int e_idx, boolean tmp) {
        if (s_idx >= e_idx) return;
        for (int idx=s_idx; idx<e_idx; idx++) {
            if (pre_result.get(idx) > pre_result.get(s_idx)) {
                post_result(s_idx + 1, idx, true);
                post_result(idx, e_idx, false);
                System.out.println(pre_result.get(idx));
                if (tmp) System.out.println(pre_result.get(s_idx));
                return;
            }
        }
        post_result(s_idx + 1, e_idx, true);
        if (tmp) System.out.println(pre_result.get(s_idx));
    }
}
