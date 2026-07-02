// class Solution {
//     public int numberOfPoints(List<List<Integer>> nums) {
//         HashSet<Integer> set = new HashSet<>();

//         for(List<Integer> num : nums){
//             int start = num.get(0);
//             int end = num.get(1);

//             for(int i = start ; i <=  end ;i++){
//                 set.add(i);
//             }
//         }

//         return set.size();
//     }
// }

class Solution {
    public int numberOfPoints(List<List<Integer>> nums) {
        boolean[] arr = new boolean[101];

        for(List<Integer> num : nums){
            int start = num.get(0);
            int end = num.get(1);

            for(int i = start ; i <=  end ;i++){
                arr[i] = true;
            }
        }

        int ans = 0;
        for(boolean i : arr){
            if(i) ans++;
        }

        return ans;
    }
}