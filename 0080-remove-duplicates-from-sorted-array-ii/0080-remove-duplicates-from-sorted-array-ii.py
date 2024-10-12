class Solution:
        #We will have an index count and an occurance count
    #loop through the range of length of nums
    #if the current number is the same as the previous nums - 1 then the occurance goes up by one 
    #else the occurance stays the same 
    #if occurance is less than or equal to 2 modify that number inplace by nums[index] = num[i]
    #and move index + 1
    #return the index
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        oc = 1
        
        for i in range(1,len(nums)):
            if nums[i] == nums[i - 1]:
                oc += 1         
            else:
                oc = 1

            if oc <= 2:
                nums[index] = nums[i]                
                index += 1
            
        return index
        