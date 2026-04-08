class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # the data structure to use is the Python set()
        duplicate_catcher = set()   
        for number in nums:
            if number in duplicate_catcher:
                return True
            else:
                duplicate_catcher.add(number)
        return False
                