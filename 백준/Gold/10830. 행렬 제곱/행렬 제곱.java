import java.util.*;
import java.io.*;
public class Main {

    final static int MOD = 1000;
    public static int N;
    public static int[][] origin;	// A^1 일 때의 배열(초기 배열)

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        N = Integer.parseInt(st.nextToken());
        long B = Long.parseLong(st.nextToken());	// 타입 주의
        origin = new int[N][N];
        
        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            for(int j = 0; j < N; j++) {
                origin[i][j] = Integer.parseInt(st.nextToken()) % MOD;
            }
        }

        int[][] result = pow(origin, B);
        
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < N; i++) {
            for(int j = 0; j < N; j++) {
                sb.append(result[i][j]).append(' ');
            }
            sb.append('\n');
        }
        System.out.println(sb);
    }

    public static int[][] pow(int[][] A, long exp) {
        if(exp == 1L) {
            return A;
        }
        
        int[][] ret = pow(A, exp / 2);
        
        ret = multiply(ret, ret);
        
        if(exp % 2 == 1L) {
            ret = multiply(ret, origin);
        }
        
        return ret;
    }

    public static int[][] multiply(int[][] o1, int[][] o2) {
        int[][] ret = new int[N][N];
        for(int i = 0; i < N; i++) {
            for(int j = 0; j < N; j++) {
                for(int k = 0; k < N; k++) {
                    ret[i][j] += o1[i][k] * o2[k][j];
                    ret[i][j] %= MOD;
                }
            }
        }
        return ret;
    }
}