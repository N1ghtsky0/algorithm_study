class Solution {
    public int[] solution(int n) {
        int maximum = n * (n + 1) / 2;
        int[][] triangle = new int[n][];
        for (int _n = 0; _n < n; _n++) {
            triangle[_n] = new int[_n + 1];
        }

        int row = 0;
        int col = 0;
        String direction = "down";

        for (int step = 1; step <= maximum; step++) {
            triangle[row][col] = step;
            if ("down".equals(direction)) {
                if (row + 1 == n || triangle[row + 1][col] != 0) {
                    direction = "right";
                    col++;
                }
                else { row++; }
            } else if ("right".equals(direction)) {
                if (col + 1 == n || triangle[row][col + 1] != 0) {
                    direction = "up";
                    row--; col--;
                }
                else { col++; }
            } else {
                if (triangle[row - 1][col - 1] != 0) {
                    direction = "down";
                    row++;
                }
                else { row--; col--; }
            }
        }
        
        int[] result = new int[maximum];
        for (int i = 0; i < n; i++) {
            System.arraycopy(triangle[i], 0, result, i * (i + 1) / 2, i + 1);
        }
        return result;
    }
}