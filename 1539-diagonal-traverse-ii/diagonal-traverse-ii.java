class Solution {
    public int[] findDiagonalOrder(List<List<Integer>> nums) {
        List<Integer> resList = new ArrayList<>();
        LinkedList<int[]> q = new LinkedList<>();
        q.offer(new int[]{0, 0});

        while (!q.isEmpty()) {
            int[] p = q.poll();
            resList.add(nums.get(p[0]).get(p[1]));

            if (p[1] == 0 && p[0] + 1 < nums.size()) {
                q.offer(new int[]{p[0] + 1, 0});
            }

            if (p[1] + 1 < nums.get(p[0]).size()) {
                q.offer(new int[]{p[0], p[1] + 1});
            }
        }

        // Convert List<Integer> to int[]
        int[] res = new int[resList.size()];
        for (int i = 0; i < resList.size(); i++) {
            res[i] = resList.get(i);
        }

        return res;         
    }
}