class Solution:
    def findMin(self, nums: List[int]) -> int:
        # first try the trivial 0(n) - linear time
        min_value = nums[0]
        if nums[0] == 0:
            return nums[0]

        for i in nums:
            if i < min_value:
                min_value = i
        return min_value