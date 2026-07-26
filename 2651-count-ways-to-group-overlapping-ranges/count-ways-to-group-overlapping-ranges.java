class Solution {
    public int countWays(int[][] ranges) {
        Arrays.sort(ranges,(a,b)->Integer.compare(a[0],b[0]));
        int res=2, max=ranges[0][1], mod=1_000_000_007;
        for(int i=1;i<ranges.length;i++){
            if(ranges[i][0]>max){
                res=(res*2)%mod;
            }
            max=Math.max(max,ranges[i][1]);
        }
        return res;
    }
}