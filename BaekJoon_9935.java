// Baekjoon 9935
// https://www.acmicpc.net/problem/9935

import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String string = br.readLine();
        String bomb = br.readLine();
        br.close();

        StringBuilder answer = new StringBuilder();
        for (int i=0; i<string.length(); i++) {
            char c = string.charAt(i);
            answer.append(c);
            if (answer.length() >= bomb.length()) {
                if (answer.substring(answer.length()-bomb.length(), answer.length()).equals(bomb))
                    answer.delete(answer.length()-bomb.length(), answer.length());
            }
        }
        System.out.println((answer.length()==0)?"FRULA":answer);
    }
}
