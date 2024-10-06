class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
            # Use a deque to store indices of elements in the window in decreasing order of their values
        q = collections.deque()

        # Left and right pointers for the window
        l = r = 0

        # Iterate while the right pointer is within the array bounds
        while r < len(nums):
        # Maintain a decreasing order in the deque:
        # If the current element is greater than elements at indices in the deque,
        # pop them from the deque as they are no longer useful for max calculation
            while q and nums[q[-1]] < nums[r]:
                q.pop()
    
            # Append the current index to the deque
            q.append(r)
    
            # Remove the left index from the deque if it is out of the window's range
            if l > q[0]:
                q.popleft()
    
            # Once the window size reaches k, add the maximum element (at deque's front) to the output
            if (r + 1) >= k:
                output.append(nums[q[0]])
                # Move the left pointer to slide the window
                l += 1
    
            # Move the right pointer to expand the window
            r += 1

            # Return the result containing all the maximums of the sliding windows
        return output
            