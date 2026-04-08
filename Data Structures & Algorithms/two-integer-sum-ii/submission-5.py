class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # since we have 0(1) memory constraint, we will not use a data structure.
        # since the array is sorted, we can use two-pointers; one pointer at the beginning
        # the other pointer at the end.

        L, R = 0, len(numbers) -1

        while L < R:
            curr_sum = numbers[L] + numbers[R]

            if curr_sum == target:
                return [L + 1, R + 1]
            elif curr_sum < target:
                L += 1
            else:
                R -= 1
        return []