class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        oc = 1
        index = 1
        
        
        for i in range(1,len(nums)):
            if nums[i] == nums[i - 1]:
                oc += 1
            else:
                oc = 1
                
                
            if oc <= 2:
                nums[index] = nums[i]   
                index += 1
                
                
        return index
            
        