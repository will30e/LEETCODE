class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Sort the points based on their starting position.
        # This helps in grouping overlapping intervals together.
        points.sort()

        # Initialize the result with the total number of balloons (arrows).
        # In the worst case, each balloon requires a separate arrow.
        res = len(points)

        # Keep track of the previous interval (initially the first one).
        prev = points[0]

        # Iterate through the rest of the points, starting from the second one.
        for i in range(1, len(points)):
            cur = points[i]  # Current balloon interval.

            # Check if the current balloon overlaps with the previous one.
            if cur[0] <= prev[1]:
                # If they overlap, we can shoot them with one arrow.
                res -= 1  # Decrease the arrow count as one arrow covers both.

                # Update the previous interval to the intersection of the two.
                # This ensures we always track the smallest range of overlap.
                prev = [cur[0], min(cur[1], prev[1])]

            else:
                # If they don't overlap, update `prev` to the current interval.
                # A new arrow will be needed for this new group.
                prev = cur

        # Return the minimum number of arrows needed to burst all balloons.
        return res
