class Solution:
    def findMin(self, nums: List[int]) -> int:
        # first try the trivial 0(n) - linear time
        min_value = nums[0]

        for i in nums[1:]:
            if i < min_value:
                min_value = i
        return min_value