class Solution {
    private int lineSweep(int n, int[][] arr, int idx, List<List<Integer>> ranges){
        int curr_y = arr[idx][0], tmp[] = new int[]{arr[idx][1], arr[idx][2]};
        idx++;
        for(; idx < n && curr_y == arr[idx][0]; idx++){
            if(arr[idx][1] < tmp[1]) return -1;
            if(tmp[1] == arr[idx][1]) {
                tmp[1] = arr[idx][2];
                continue;
            } else {
                ranges.add(List.of(tmp[0], tmp[1]));
                tmp = new int[]{arr[idx][1], arr[idx][2]};
            }
        }

        ranges.add(List.of(tmp[0], tmp[1]));
        return idx;
    }
    public boolean isRectangleCover(int[][] A) {
        int n = A.length, idx = 0, start[][] = new int[n][], end[][] = new int[n][];
        for(int[] a: A){
            start[idx] = new int[]{a[1], a[0], a[2]};
            end[idx++] = new int[]{a[3], a[0], a[2]};
        }

        Comparator<int[]> sortComparator = 
            (a, b) -> a[0] == b[0] ? Integer.compare(a[1], b[1]) : Integer.compare(a[0], b[0]);
        Arrays.sort(start, sortComparator);
        Arrays.sort(end, sortComparator);

        int stIdx = 0, enIdx = 0;
        List<List<Integer>> stRanges = new ArrayList<>(), enRanges = new ArrayList<>();

        stIdx = lineSweep(n, start, stIdx, stRanges);
        if(stIdx == -1 || stRanges.size() > 1) return false;

        while(stIdx < n){
            int curr_y = start[stIdx][0];
            stRanges.clear();
            stIdx = lineSweep(n, start, stIdx, stRanges);
            if(stIdx == -1) return false;
            
            if(curr_y != end[enIdx][0]) return false;
            enRanges.clear();
            enIdx = lineSweep(n, end, enIdx, enRanges);
            if(enIdx == -1) return false;

            if(!stRanges.equals(enRanges)) return false;
        }

        enRanges.clear();
        enIdx = lineSweep(n, end, enIdx, enRanges);
        if(enIdx == -1 || enRanges.size() > 1 || enIdx != n) return false;
        
        return true;
    }
}