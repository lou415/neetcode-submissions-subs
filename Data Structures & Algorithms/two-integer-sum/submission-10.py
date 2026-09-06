class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for idx, value in enumerate(nums):
            difference = target - value
            if difference in seen:
                return [seen[difference], idx]
            seen[value] = idx

        return []

