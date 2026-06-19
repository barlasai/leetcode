class Solution {
    public long waysToBuyPensPencils(int total, int cost1, int cost2) {
        int[] cost={cost1,cost2};
        return 1+ waysToBuyPensPencils(total,cost,0);
    }
    public long waysToBuyPensPencils(int total, int[] cost, int si){
        if(si==cost.length-1){
            return total/cost[si];
        }
        if(total==0){
            return 0;
        }
        long pick=0;
        long notPick=waysToBuyPensPencils(total,cost,si+1);
        if(total-cost[si]>=0){
           pick = 1 + waysToBuyPensPencils(total-cost[si],cost,si);
        }
        return pick+notPick;
    }
}