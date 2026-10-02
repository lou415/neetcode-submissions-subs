class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # this is a linear data structure, so we can use two pointers.
        L, R = 0, len(s) - 1

        # use a temp variable so that we don't lose any characters
        temp_variable = ""
        while L < R:
            temp_variable = s[L]
            s[L] = s[R]
            s[R] = temp_variable
            L += 1
            R -= 1
        return s