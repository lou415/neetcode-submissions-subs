class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # THE EQUATION = target - curr.val = some #
        # We use the python dict, which uses the hash table ds, to
        # implement MAP ADT to see if that some # is in the dict.

        # because lookup is O(1), and algebraically, curr.val + some #
        # is the target number.

        ans_dict = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in ans_dict:
                return [ans_dict[diff], i]
            ans_dict[n] = i
        return





