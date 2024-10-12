class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []  # This will store the result.

        # Insert all intervals, handling overlaps with `newInterval`.
        for start, end in intervals:
            # Get the last end of the current result, if any intervals exist.
            if res:
                lastEnd = res[-1][1]
            else:
                lastEnd = None  # No intervals yet.

            # If the new interval is completely before the current one.
            if newInterval[1] < start:
                res.append(newInterval)  # Insert the new interval.
                return res + intervals[intervals.index([start, end]):]  # Add remaining intervals.

            # If the new interval is after the current one, just add the current interval.
            elif newInterval[0] > end:
                res.append([start, end])

            # If there is an overlap, merge the intervals.
            else:
                newInterval = [min(newInterval[0], start), max(newInterval[1], end)]

        # If the new interval was not added during the loop, add it at the end.
        res.append(newInterval)
        return res
