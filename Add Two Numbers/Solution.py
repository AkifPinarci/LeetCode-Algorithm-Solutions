# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

        
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        cur1 = l1
        cur2 = l2
        string1 = ""
        string2 = ""
        while cur1:
            string1 += str(cur1.val)
            cur1 = cur1.next
            
        while cur2:
            string2 += str(cur2.val)
            cur2 = cur2.next
        
        string3 = str(int(string1[::-1]) + int(string2[::-1]))
        string3 = string3[::-1]
        result = cur3 = ListNode(string3[0])
        string3 = string3[1:]
        for i in string3:
            cur3.next = ListNode(int(i))
            cur3 = cur3.next

        return result