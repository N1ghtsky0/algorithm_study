// Baekjoon 1967
// https://www.acmicpc.net/problem/1967
  
import java.util.*;
import java.io.*;
public class Main {
    static int answer = 0;
    static HashMap<Integer, List<int[]>> tree = new HashMap<>();
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());
        for (int N=0; N<n-1; N++) {
            st = new StringTokenizer(br.readLine());
            int p, c, t;
            p = Integer.parseInt(st.nextToken());
            c = Integer.parseInt(st.nextToken());
            t = Integer.parseInt(st.nextToken());
            List<int[]> branch = tree.getOrDefault(p, new ArrayList<>());
            branch.add(new int[]{c, t});
            tree.put(p, branch);
        }
        br.close();

        tree.put(0, new ArrayList<>());
        tree.get(0).add(new int[] {1, 0});  // 1(최상위 부모)까지 모두 살펴보기 위해서 가중치 0이고 1과 연결된 0번 노드 생성
        dfs(0);
        System.out.println(answer);
    }

    static int dfs(int parent) {
        if (!tree.containsKey(parent))
            return 0;
        List<Integer> tmp = new ArrayList<>();
        tmp.add(0);
        for (int[] child : tree.get(parent)) {
            tmp.add(dfs(child[0]) + child[1]);
        }
        tmp.sort(Comparator.reverseOrder());
        int ans = tmp.get(0) + tmp.get(1);
        if (ans > answer) answer = ans;
        return tmp.get(0);
    }
}
