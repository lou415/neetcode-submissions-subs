class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # create implement set ADT using python's set to check for duplicates

        duplicate_checker = set()
        max_distance = 0
        L = 0

        for R in range(len(s)):
            while s[R] in duplicate_checker:
                duplicate_checker.remove(s[L])
                L += 1
            duplicate_checker.add(s[R])
            max_distance = max(max_distance, R - L +1)
        
        return max_distance