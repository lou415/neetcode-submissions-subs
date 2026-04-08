class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # since we have 0(1) memory constraint, we will not use a data structure.
        # since the array is sorted, we can use two-pointers; one pointer at the beginning
        # the other pointer at the end.

        L, R = 0, len(numbers) -1

        for i in range(len(numbers)):
            if numbers[L] + numbers[R] > target:
                R -= 1
            if numbers[L] + numbers[R] < target:
                L += 1
            if numbers[L] + numbers[R] == target:
                return [L + 1, R + 1]
        return []