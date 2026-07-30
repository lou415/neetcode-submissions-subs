class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicateChecker = set()
        for num in nums:
            if num not in duplicateChecker:
                duplicateChecker.add(num)
            else:
                return True
        return False
        