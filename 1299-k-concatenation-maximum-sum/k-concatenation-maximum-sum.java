class Solution {
    long total;
    public int kConcatenationMaxSum(int[] arr, int k) {
        int len = arr.length;
        int MOD = 1_000_000_007;

        if(k == 1){
            long ans = finderMax(arr, len, len);
            return (int)(ans%MOD);
        }

        long ans1 = finderMax(arr, len*2, len);

        long ans2 = 0;
        if(total > 0) {
            long[] val = new long[2];
            IndMax(arr, 0, len, val);
            ans2 += val[0];
            ans2 += val[1];
            
            ans2 += ((k-2)*total)%MOD;
        }

        return (int) Math.max(ans1, ans2)%MOD;
    }

    public void IndMax(int[] arr, int st, int ed, long[] val){
        long max1 = 0;
        long sum1 = 0;
        long max2 = 0;
        long sum2 = 0;
        for(int i = st;i < ed;i++){
            sum1 += arr[i];
            max1 = Math.max(max1, sum1);
            
            sum2 += arr[ed-1-i];
            max2 = Math.max(max2, sum2);
        }
        
        val[0] = max1;
        val[1] = max2;
    }

    public long finderMax(int[] arr, int len, int lim){
        long sum = 0;
        long max = 0;
        long ttl = 0;
        for(int i = 0;i < len;i++){
            sum += arr[i%lim];
            if(sum < 0) sum = 0;
            max = Math.max(max, sum);
            ttl += arr[i%lim];
        }

        total = ttl/2;

        return max;
    }
}