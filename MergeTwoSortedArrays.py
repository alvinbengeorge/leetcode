# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and list2:
            while list2:
                temp1, temp2 = list1, list2
                list2 = list2.next

                if temp2.val <= temp1.val:
                    temp2.next = temp1
                    list1 = temp2
                else:
                    prev = None
                    while temp1 and temp2.val > temp1.val:
                        prev = temp1
                        temp1 = temp1.next

                    temp = prev.next
                    prev.next = temp2
                    temp2.next = temp
            return list1
        else:
            return list1 or list2 or None        
