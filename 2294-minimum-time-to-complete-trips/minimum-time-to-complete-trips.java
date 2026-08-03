class Solution {
    int[]time;
    int tt;
    public long minimumTime(int[] time, int totalTrips) {
        this.time=time;
        this.tt=totalTrips;
        long low=1,min=(int)1e9;
        for(int a:time){
            min=Math.min(min,a);
        }
        long high=min*totalTrips;
        long ans=0;
        while(low<=high){
            long mid=low+(high-low)/2;
            if(helper(mid)){
                ans=mid;
                high=mid-1;
            }else{
                low=mid+1;
            }
        }
        return ans;

    }public boolean helper(long mid){
        long count=0;
        for(int i=0;i<time.length;i++){
            count+=(mid/time[i]);
        }
        return count>=tt;
    }
}