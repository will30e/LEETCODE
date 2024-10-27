class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        
        fp, sp, lp = m - 1, n - 1, m + n - 1
        
        
        
        while fp >= 0 and sp >= 0:
            if nums1[fp] > nums2[sp]:
                nums1[lp] = nums1[fp]
                fp -= 1
                
            else:
                nums1[lp] = nums2[sp]
                sp -= 1
            lp -= 1
       
    
    
        if sp >= 0:    
            nums1[:sp + 1] = nums2[:sp + 1]