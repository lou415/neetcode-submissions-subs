class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string_one_dict = {}
        string_two_dict = {}

        for i in s:
            if i not in string_one_dict:
                string_one_dict[i] = 1
            else:
                string_one_dict[i] += 1
        for j in t:
            if j not in string_two_dict:
                string_two_dict[j] = 1
            else:
                string_two_dict[j] += 1
        return string_one_dict == string_two_dict