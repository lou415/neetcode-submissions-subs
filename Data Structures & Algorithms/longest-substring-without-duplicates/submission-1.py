class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # create implement set ADT using python's set to check for duplicates

        if not s:
            return 0

        checker = set()

        # creating the pointers for sliding window
        L = 0
        result = 0
        for r in range(len(s)):
            while s[r] in checker:
                checker.remove(s[L])
                L += 1
            checker.add(s[r])
            result = max(result, r-L + 1)
        return result