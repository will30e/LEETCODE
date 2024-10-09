class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # First, sort the intervals by the starting time of each interval.
        # Sorting ensures that overlapping intervals are adjacent.
        intervals.sort(key=lambda i: i[0])

        # Initialize the 'output' list with the first interval.
        output = [intervals[0]]

        # Iterate through the rest of the intervals (starting from the second one)
        for start, end in intervals[1:]:
            # Get the end of the last interval in the output list
            lastEnd = output[-1][1]

            # Check if the current interval overlaps with the last interval in the output list
            if start <= lastEnd:
                # If it overlaps, merge the intervals by updating the end of the last interval
                # to the maximum end time between the two overlapping intervals
                output[-1][1] = max(lastEnd, end)
            else:
                # If it does not overlap, add the current interval to the output list
                output.append([start, end])

        # Return the merged list of intervals
        return output
        