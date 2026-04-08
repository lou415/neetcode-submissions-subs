class Solution:
    def findMin(self, nums: List[int]) -> int:
        # L, R = 0, len(nums) - 1

        # while(nums[L] > nums[R]):
        #     L += 1
        # return nums[L]

        L, R = 0, len(nums) - 1

        while (L < R):
            mid = (L+R) // 2
            if nums[mid] > nums[R]:
                L = mid + 1
            else:
                R = mid
        return nums[L]