class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram = {}
        anagram_2 = {}
        for i in s:
            if i not in anagram:
                anagram[i] = 1
            else:
                anagram[i] += 1
        for x in t:
            if x not in anagram_2:
                anagram_2[x] = 1
            else:
                anagram_2[x] += 1 
        if anagram == anagram_2:
            return True
        else:
            return False
        
            