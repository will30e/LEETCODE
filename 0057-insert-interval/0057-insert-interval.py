class Solution:
    #start with a result
    #loop through all the intervals by range
    #if the 2 values in new intervals is less than the first value in intervals
    #if the 1 value in new intervals is greater than the second value in the intervals
    # if both are false meaning no overlap append it to the res
    #else create a new interval with the first being the minimun between the current interval and the new interval and the second being the maximum between the current interval and the new interval
    #return the res
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []  # This will store the result.

        # Iterate through all intervals.
        for i in range(len(intervals)):
            # Case: New interval ends before the current interval starts.
            if newInterval[1] < intervals[i][0]:
                # Add the new interval to the result and return the remaining intervals.
                res.append(newInterval)
                return res + intervals[i:]

            # Case: New interval starts after the current interval ends.
            elif newInterval[0] > intervals[i][1]:
                # Add the current interval to the result as-is.
                res.append(intervals[i])

            # Case: New interval overlaps with the current interval.
            else:
                # Merge the intervals by taking the minimum start and maximum end.
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        # If the new interval was not added during the loop, add it now.
        res.append(newInterval)
        return res
