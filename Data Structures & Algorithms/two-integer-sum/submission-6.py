class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use a dictionary to hold the value as key and index as value.
        # we can do this automatically with enumerate in Python.
        dictionary = {}

        for i, num in enumerate(nums):
            # create the complement equation ==> complement = target - nums[i]
            complement = target - nums[i] 
            if complement in dictionary:
                return [dictionary[complement], i]
            dictionary[num] = i
        return []
        
        




