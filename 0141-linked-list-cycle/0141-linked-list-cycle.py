# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        #we will check if the head is None
        #Create 2 pointers s,f
        # if they are not the same then we will move both of them
        #s will be twice as slow as fast

        if head == None:
            return False
        
        s = head
        f = head.next
        
        
        while s != f:
            if f == None or f.next == None:
                return False
            
            s = s.next
            f = f.next.next
            
        return True