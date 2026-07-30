class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequenceSet = set(nums)
        longest = 0

        for num in nums:
            # is this the start of a sequence?
            if (num - 1) not in sequenceSet:
                # this means this could be the start of a sequence
                # and that means we'll want to keep track just in case.
                length = 0
                while (num + length) in sequenceSet:
                    length += 1
                longest = max(length, longest)
        return longest
                 