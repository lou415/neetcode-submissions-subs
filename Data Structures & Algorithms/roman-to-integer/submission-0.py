class Solution:
    def romanToInt(self, s: str) -> int:
        # 1) Populate the hash table with the values
            # - populate as you iterate, rather than doing it at once.
                # - This may not be the best choice as you would have
                # to write at most 7 if statements to map the elements
                # to their corresponding values. 
            # populate the hashtable up-front.
        # largest to smallest: add them up.
        # smallest to largest: subtract them.
        roman_hash = {"I":1, "V": 5, 
                      "X":10, "L":50,
                      "C":100, "D":500, "M":1000}
        res = 0
        for char in range(len(s)):
            # checking if it is in bounds
            if char + 1 < len(s) and roman_hash[s[char]] < roman_hash[s[char+1]]:
                res -= roman_hash[s[char]]
            else:
                res += roman_hash[s[char]]
        return res
                
    