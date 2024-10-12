class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        res = []
        start = nums[0]

        for i in range(1, len(nums)):
            # Check if the current number is not consecutive
            if nums[i] != nums[i - 1] + 1:
                # If start equals nums[i-1], it's a single number range
                if start == nums[i - 1]:
                    res.append(str(start))
                else:
                    res.append(f"{start}->{nums[i - 1]}")
                start = nums[i]  # Reset start

        # Add the last range
        if start == nums[-1]:
            res.append(str(start))
        else:
            res.append(f"{start}->{nums[-1]}")

        return res
