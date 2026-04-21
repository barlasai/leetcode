class Solution(object):
    def findPeakElement(self, nums):
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if mid == 0:
                return 0 if nums[0] >= nums[1] else 1
            if mid == end:
                return end - 1 if nums[end - 1] >= nums[end - 2] else end - 2

            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid
            if nums[mid] < nums[mid - 1]:
                end = mid - 1
            else:
                start = mid + 1
        return start