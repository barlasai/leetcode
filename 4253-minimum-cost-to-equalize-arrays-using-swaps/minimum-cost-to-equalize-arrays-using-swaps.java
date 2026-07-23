class Solution {
    public int minCost(int[] nums1, int[] nums2) {
        HashMap<Integer, Integer> mp = new HashMap<>();

        for (int x : nums1) 
            mp.put(x, mp.getOrDefault(x, 0) + 1);

        for (int x : nums2) 
            mp.put(x, mp.getOrDefault(x, 0) - 1);

        int ans = 0;
        for (int c : mp.values()) {
            if ((Math.abs(c) & 1) == 1) return -1;
            ans += Math.abs(c) / 2;
        }

        return ans / 2;
    }
}