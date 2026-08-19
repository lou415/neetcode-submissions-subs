class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        # sorts in place O(log n)
        nums.sort()

        for idx, value in enumerate(nums):
            # can't resuse same value in same position.
            # if i is not the first value
            # and it is equivalent
            if idx > 0 and value == nums[idx-1]:
                # indicates duplicate value
                continue
            l, r = idx + 1, len(nums) - 1
            while l < r:
                threeSum = value + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    result.append([value, nums[l], nums[r]])
                    # updating the pointers
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return result