class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
 
        def solve(left, right):
            if left > right: return None
            m = (left + right)//2
            return TreeNode(nums[m], solve(left,m-1), solve(m+1,right))
        return solve(0, len(nums)-1)