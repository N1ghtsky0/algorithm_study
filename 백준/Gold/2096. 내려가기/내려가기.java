import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        int N = read();
        int[] dp = new int[6];
        for (int n=0; n<N; n++) {
            int[] input = new int[3];

            for (int i=0; i<3; i++)
                input[i] = read();

            int[] dp_ = new int[6];
            dp_[0] = input[0] + Math.min(dp[0], dp[1]);
            dp_[1] = input[1] + Math.min(dp[0], Math.min(dp[1], dp[2]));
            dp_[2] = input[2] + Math.min(dp[1], dp[2]);
            dp_[3] = input[0] + Math.max(dp[3], dp[4]);
            dp_[4] = input[1] + Math.max(dp[3], Math.max(dp[4], dp[5]));
            dp_[5] = input[2] + Math.max(dp[4], dp[5]);

            dp = dp_;
        }
        System.out.println(Math.max(dp[3], Math.max(dp[4], dp[5])) + " " + Math.min(dp[0], Math.min(dp[1], dp[2])));
    }

    static int read() throws IOException {
        int c, n = System.in.read() & 15;
        while ((c = System.in.read()) > 32)
            n = (n << 3) + (n << 1) + (c & 15);
        return n;
    }
}