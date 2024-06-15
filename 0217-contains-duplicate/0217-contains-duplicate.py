class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for i,n in enumerate(nums):
            
            if n in dic:
                return True
            
            dic[n] = i

           
        return False 
        

        