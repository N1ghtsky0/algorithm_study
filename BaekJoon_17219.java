// Baekjoon 17219
// https://www.acmicpc.net/problem/17219

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        HashMap<String, String> map = new HashMap<>();

        String[] NM = br.readLine().split(" ");
        for (int n=0; n<Integer.parseInt(NM[0]); n++) {
            String[] info = br.readLine().split(" ");
            map.put(info[0], info[1]);
        }

        for (int m=0; m<Integer.parseInt(NM[1]); m++) {
            String info = br.readLine();
            System.out.println(map.get(info));
        }
        
        br.close();
    }
}
