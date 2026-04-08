class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i : i[0])
        result = [intervals[0]]

        # this unpacks the interval start and end into tuples
        for start, end in intervals[1:]:
            # index the last interval, then take the last value in that interval and set it to last_end.
            last_end = result[-1][1]
            # if the start of the new interval is <= the end of the previous one, it overlaps
            if start <= last_end:
                # find which value is bigger
                result[-1][1] = max(last_end, end)
            else:
                # simply append the interval
                result.append([start,end])
        return result