class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen_list = set()
        for x in nums1:
            if x in nums2:
                seen_list.add(x)
        return list(seen_list)