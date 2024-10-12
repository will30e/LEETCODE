class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # If the new interval is before the current one, insert it and return.
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]

            # If the new interval is after the current one, just add the current interval.
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])

            # If the new interval overlaps with the current one, merge them.
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        # If the new interval wasn't inserted during the loop, append it at the end.
        res.append(newInterval)
        return res
