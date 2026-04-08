class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # we first iterate through nums to see if iterator is
        # equal to val.
        vals = []
        for num in nums:
            if num == val:
                continue
            vals.append(num)
        for i in range(len(vals)):
            nums[i] = vals[i]
        return len(vals)
            

        