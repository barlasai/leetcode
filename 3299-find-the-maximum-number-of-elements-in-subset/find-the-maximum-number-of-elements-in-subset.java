class Solution {
    public int maximumLength(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int num : nums) {
            map.merge(num, 1, Integer::sum);
        }

        int ans = map.getOrDefault(1, 1);

        // Number of 1's used must be odd
        if (ans % 2 == 0) {
            ans--;
        }

        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            int num = entry.getKey();
            int freq = entry.getValue();

            if (num == 1) continue;

            if (freq >= 2) {
                int levels = 1;
                long cur = (long) num * num;

                while (cur < Integer.MAX_VALUE &&
                       map.getOrDefault((int) cur, 0) >= 2) {
                    cur *= cur;
                    levels++;
                }

                if (cur < Integer.MAX_VALUE &&
                    map.getOrDefault((int) cur, 0) == 1) {
                    levels++;
                }

                ans = Math.max(ans, 2 * levels - 1);
            }
        }

        return ans;
    }
}