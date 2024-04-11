class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height) - 1

        while l < r:
            area = (r - l) * min(height[r], height[l])
            res = max(res, area)

            if height[r] > height[l]:
                l += 1
            else:
                r -=1

        return res

        
 