# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list  = ListNode()
        merged_head = merged_list

        while  list1 and  list2 :
            new_node = ListNode()
            
           
            if  list1.val >=  list2.val:
                new_node.val = list2.val
                new_node.next = None
                list2 = list2.next 
            else:
                new_node.val = list1.val
                new_node.next = None
                list1 = list1.next  
           
            merged_head.next = new_node
            merged_head = merged_head.next
            
        merged_head.next = list1 or list2
           
        return merged_list.next