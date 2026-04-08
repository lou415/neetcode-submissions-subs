class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        frequency = {}
        for number in nums:
            frequency[number] = frequency.get(number, 0) + 1
        sorted_items = sorted(frequency.items(), key = lambda x : x[1], reverse=True)

        return [item[0] for item in sorted_items[:k]]
# dictionary .items ==> tuple(key, value)
# we want to sort this tuple, but by the values, not the keys.
    # this is why we use sorted and a custom key, which is a lambda function
    # sorted(items, key = some function)
# lambda syntax ==> lambda parameters : expression to return