class Solution {
    public int subarraysWithKDistinct(int[] nums, int k) {
        return check(nums,k)-check(nums,k-1);
    }
    public int check(int [] nums,int k){
        int l=0;
        int r=0;
        int cnt=0;
        HashMap<Integer,Integer> h=new HashMap<>();

        for(r=0;r<nums.length;r++){
          h.put(nums[r],h.getOrDefault(nums[r],0)+1);
          while(h.size()>k){
            h.put(nums[l],h.getOrDefault(nums[l],0)-1);
            if(h.get(nums[l])==0)
             h.remove(nums[l]);
             l++;
          }
          
           cnt+=r-l+1;

        }
        return cnt;
    }
    
}