class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mapST, mapTS = {}, {}

        for i in range(len(s)):
            # get the character at index i for both of the strings
            c1, c2 = s[i], t[i]

            if ((c1 in mapST and mapST[c1] != c2) or (c2 in mapTS and mapTS[c2] != c1)):
                return False

            # this is how we map our characters
            mapST[c1] = c2
            mapTS[c2] = c1
        return True