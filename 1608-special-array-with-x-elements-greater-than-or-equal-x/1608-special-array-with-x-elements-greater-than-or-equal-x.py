class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        
        for i in range(n):
            if i < nums[i] and (i == n - 1 or i + 1 > nums[i + 1]):
                return i + 1
                
        return -1