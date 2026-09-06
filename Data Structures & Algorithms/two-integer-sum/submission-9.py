class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for idx, value in enumerate(nums):
            difference = target - value
            if difference in indices:
                return [indices[difference], idx]
            indices[value] = idx

        

