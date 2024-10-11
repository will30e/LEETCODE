class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        output = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            
            if diff in output:
                return [output[diff], i]
            
            output[n] = i
        