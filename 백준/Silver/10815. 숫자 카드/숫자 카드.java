import java.util.Arrays;
import java.util.Scanner;

public class Main {
    static int N, M;
    
    static int binary_search(long[] cards, long target) {
        int min_idx, max_idx, middle_idx;
        min_idx = 0;
        max_idx = N-1;
        while (min_idx <= max_idx) {
            middle_idx = (min_idx + max_idx) / 2;
            if (cards[middle_idx] == target)
                return 1;
            else if (cards[middle_idx] < target)
                min_idx = middle_idx + 1;
            else
                max_idx = middle_idx - 1;
        }
        return 0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        long[] cards = new long[N];
        for (int i = 0; i < N; i++)
            cards[i] = sc.nextInt();
        Arrays.sort(cards);

        M = sc.nextInt();
        long[] targets = new long[M];
        for (int i = 0; i < M; i++)
            targets[i] = sc.nextInt();

        for (long target : targets) {
            System.out.print(binary_search(cards, target) + " ");
        }
    }
}