import java.util.Arrays;

class Solution {
    // dp[i]: Can number i be formed?
    static boolean[] dp = new boolean[4001];

    public static boolean[] subsequenceSumAfterCapping(int[] nums, int k) {
        // Sort nums so we can easily to find how many elements are greater than x in O(1)
        Arrays.sort(nums);
        int n = nums.length;

        // Initialize dp
        Arrays.fill(dp, false);
        dp[0] = true;

        // Index for nums
        int p = 0;

        // answer array
        boolean[] ans = new boolean[n];

        // Travser each x
        for (int x = 1; x <= n; x++) {
            while (p < n && nums[p]< x){
                // Similar to knapsack with space optimization 
                for (int j = k; j >= nums[p]; j--) dp[j] |= dp[j-nums[p]];
                p++;
            }
            // number of elements which are greater (or equal to) than
            // x (change to x)
            int cnt = n-p;

            // Multiple knapsacks
            for (int j = 0; j <= cnt; j++) {
                // Pick j knapsacks(each has weight of x)
                int weight = x *j;

                if(k < weight)break;
                // We can form dp[k-weight], so we can form dp[k] 
                // by choosing j knapsacks(each has weight of x)
                if(dp[k-weight]){
                    ans[x -1] = true;
                    break;
                }
            }
        }

        return ans;
    }

}