class Solution {
    public long countSubarrays(int[] nums, long k) {
        int l=0;
        long count=0;
        long sum=0;
        for(int r=0;r<nums.length;r++){
            //s1 : add in the window
            sum+=nums[r];
            //s2 : make validate
            while((sum*(r-l+1))>=k){
                sum-=nums[l];
                l++;
            }
            //s3 : racking
            count+=(r-l+1);
        }
        return count;
    }
}