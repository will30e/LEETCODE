# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

    #we will check if the head is None
    #Create 2 pointers s,f
    # if head is None return false
    #s will be twice as slow as fast
    # if f is None or f.next is None return return false
    # move both pointers before returning true
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        
        s = head
        f = head.next
        
        while s != f:
            if f is None or f.next is None:
                return False
                
            s = s.next
            f = f.next.next

        return True

            