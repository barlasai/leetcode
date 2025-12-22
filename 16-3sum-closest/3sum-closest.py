class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        sm=float("inf")
        for i in range(len(nums)-2):
            j=i+1
            k=len(nums)-1
            while j<k:
                csm=nums[i]+nums[j]+nums[k]
                if abs(csm-target)<abs(sm-target):
                    sm=csm
                    
                if csm<target:
                    j+=1
                elif csm>target:
                    k-=1
                else:
                    return csm
        return sm
        