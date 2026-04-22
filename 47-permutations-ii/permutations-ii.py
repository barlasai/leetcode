class Solution(object):
    def permuteUnique(self, nums):
        nums.sort()  # optional but helpful
        result = []
        n = len(nums)

        def run(start):
            if start == n:
                result.append(nums[:])
                return

            seen = set()
            for i in range(start, n):
                if nums[i] in seen:
                    continue
                seen.add(nums[i])

                nums[start], nums[i] = nums[i], nums[start]
                run(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        run(0)
        return result