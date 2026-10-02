class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # we can use two pointers for this 
        L, R = 0, len(heights) - 1

        # creating the max area variable
        current_max_area = 0

        # making sure the two pointers don't cross each other.
        while L < R:
            max_area = min(heights[L], heights[R]) * (R-L)
            if max_area > current_max_area:
                current_max_area = max_area
            # checking for the smallest height so that we can increment the 
            # necessary pointer
            if heights[L] <= heights[R]:
                L += 1
            else:
                R -= 1
        return current_max_area
