import java.util.*;
import java.util.stream.*;

class Solution {
    public int[][] solution(int[][] dataArr, String ext, int val_ext, String sort_by) {
        List<String> extList = Arrays.asList("code", "date", "maximum", "remain");
        int extIdx = extList.indexOf(ext);
        int sortIdx = extList.indexOf(sort_by);
        List<int[]> dataList = Arrays.asList(dataArr);

        return dataList.stream()
                .filter(data -> data[extIdx] < val_ext)
                .sorted(Comparator.comparingInt(a -> a[sortIdx])).toArray(int[][]::new);
    }
}