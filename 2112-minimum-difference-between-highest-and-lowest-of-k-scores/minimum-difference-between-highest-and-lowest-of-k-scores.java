class Solution {
    public int minimumDifference(int[] nums, int k) {
        int n = nums.length;

        // Step 1: Sort the array
        Arrays.sort(nums);

        // Step 2: Initial difference
        int ans = nums[k - 1] - nums[0];

        // Step 3: Sliding window of size k
        for (int i = 0; i + k <= n; i++) {
            ans = Math.min(ans, nums[i + k - 1] - nums[i]);
        }

        // Step 4: Return result
        return ans;
    }
}