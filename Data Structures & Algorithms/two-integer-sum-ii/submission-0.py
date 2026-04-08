class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Since this is an extension of a two pointers technique
        # we can start off by intializing two pointers.
        L,R = 0, len(numbers) - 1
        while numbers[L] + numbers[R] != target:
            if numbers[L] + numbers[R] > target:
                R -= 1
            if numbers[L] + numbers[R] < target:
                L += 1
        return [L+1, R+1]