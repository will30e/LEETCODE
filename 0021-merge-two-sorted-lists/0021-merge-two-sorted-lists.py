# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to act as the starting point of the merged list
        # This helps in simplifying the merging logic
        dummy = ListNode()
        
        # 'tail' will keep track of the last node in the merged list
        tail = dummy

        # Loop until we have elements in both list1 and list2
        while list1 and list2:
            # Compare the values of the current nodes in list1 and list2
            if list1.val < list2.val:
                # If list1's value is smaller, attach it to the merged list
                tail.next = list1
                # Move to the next node in list1
                list1 = list1.next
            else:
                # Otherwise, attach list2's current node to the merged list
                tail.next = list2
                # Move to the next node in list2
                list2 = list2.next
            
            # Move the 'tail' pointer to the newly added node in the merged list
            tail = tail.next

        # If any nodes are left in list1, attach them to the merged list
        if list1:
            tail.next = list1
        
        # If any nodes are left in list2, attach them to the merged list
        elif list2:
            tail.next = list2

        # The merged list starts from 'dummy.next' (the next node after dummy)
        return dummy.next

            



            
